import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Defines the scope
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# Add Path to JSON credentials file of the Account service. Change it with yours
creds = ServiceAccountCredentials.from_json_keyfile_name("", scope)

# Authorize client with credentials
client = gspread.authorize(creds)

# Change the ID of the Google Sheet File and change with yours
sheet = client.open_by_key("").sheet1 

# Create function to insert ticket
def insert_ticket(name, cellphone, email, object, date):
    row_to_insert = [name, cellphone, email, object, date]
    sheet.append_row(row_to_insert)
