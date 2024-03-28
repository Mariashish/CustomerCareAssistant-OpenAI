import os
import time
import openai
import streamlit as st
from main import chat, ChatRequest, HTTPException, asyncio

# Change with your Assistant ID and OpenAI API Key
CHATBOT_ASSISTANT_ID = ""
OPENAI_API_KEY = ""

# Create an OpenAI client with your API key
openai_client = openai.Client(api_key=OPENAI_API_KEY)

# Retrieve the assistant you want to use
assistant = openai_client.beta.assistants.retrieve(CHATBOT_ASSISTANT_ID)

# Display an image of a robot assistant
st.image("robot_image.png", width=150)

# Create the title and subheader for the Streamlit page
st.title("Customer Care Assistant")
st.subheader("Upload a PDF and ask me anything about it!")

# Create a file input for the user to upload a PDF
uploaded_file = st.file_uploader(
    "Upload a PDF", type="pdf", label_visibility="collapsed"
)

# Allow users to input their question
user_question = st.text_input("Enter your question about the PDF:")

# If the user has uploaded a file and entered a question, start the assistant process...
if uploaded_file is not None and user_question:
    # Create a status indicator to show the user the assistant is working
    with st.status("Processing your request...", expanded=False) as status_box:
        # Upload the file to OpenAI
        file = openai_client.files.create(file=uploaded_file, purpose="assistants")

        # Create a new thread with a message that has the uploaded file's ID and the user's question
        thread = openai_client.beta.threads.create(
            messages=[
                {
                    "role": "user",
                    "content": user_question,
                    "file_ids": [file.id],
                }
            ]
        )

        # Once the run is complete, update the status box and show the content
        status_box.update(label="Complete", state="complete", expanded=True)

        response = asyncio.run(chat(ChatRequest(thread_id=thread.id, message=user_question)))
        

        if "response" in response:
            st.markdown(response["response"])
        elif "request_problem" in response and response["request_problem"]:
            st.error("OpenAI request error: process cancelled or expired.")
        else:
            st.error("Error: OpenAI request failed.")

        # Delete the uploaded file from OpenAI
        openai_client.files.delete(file.id)
