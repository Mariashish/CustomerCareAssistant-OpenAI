# Customer Care Assistant
### Overview
This repository encompasses a Customer Care Assistant project, including model selection, retrieval processes, ticket creation, UI, security measures, challenges, outcomes, and potential enhancements.

### Use Case and Tutorial
Check out the videos for usage scenarios.

### Model Choice
Chosen model: “gpt-4-turbo-preview” for its 128k context window.

### Information Retrieval Process
#### Retrieval Techniques
Incorporates information from external sources, segmenting and indexing document embeddings.

### Storage Management
Delete files to avoid unnecessary storage charges.

### Ticket Creation Mechanism and Storage Solution
#### Google Sheets Integration
Connects to Google Sheets for ticket storage.

### Ticket Creation Function
Inserts ticket details into the spreadsheet.

### FastAPI and OpenAI Integration
Uses FastAPI to create a web service. OpenAI Chatbot handles user messages and triggers ticket creation.

### Response Handling
Handles user messages and ticket creation based on context.

### Error Handling
Includes error handling for missing data and failed requests to OpenAI.

### User Friendly Interface
Built using Streamlit for easy UI development.

### Ethics Security Measures
Includes instructions to prevent disclosure of sensitive information.

### Challenges Encountered and Solutions Implemented
#### Challenges Encountered
#### Main challenge: interfacing with Streamlit.

### Solutions Implemented
Imported necessary functions into the Streamlit code.

### Project's Outcomes and Potential Improvements
#### Project’s Outcomes
Developed a virtual assistant specialized in customer care. If queries cannot be fulfilled, creates tickets for further handling.

### Potential Improvements
Endless possibilities for improving the assistant’s functions, such as order monitoring and review management.
