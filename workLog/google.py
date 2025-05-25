import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .base import BaseLogger

class GoogleSheetLogger(BaseLogger):
    def __init__(google_details, sheet_name, creds_path):
        super().__init__()
        google_details._sheet_name = sheet_name
        google_details._creds_path = creds_path
        google_details._sheet = None 

    def connect(google_details):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                google_details._creds_path, scope) 
        except Exception as e:
            print(f"Failed to load credentials: {e}")
            raise

        try:
            client = gspread.authorize(creds)
            google_details._sheet = client.open(google_details._sheet_name).sheet1
            print(f"Connected to Google Sheet: {google_details._sheet_name}")
        except Exception as e:
            print(f"Failed to connect to sheet: {e}")
            raise

    def log_entry(google_details):

        try:
            all_rows = google_details._sheet.get_all_values()
        except Exception as e:
            print(f"Failed to fetch existing records: {e}")
            raise

        for row in all_rows[1:]:
            if len(row) >= 2 and row[0] == google_details.date and row[1].lower() == google_details.name.lower():
                raise Exception(f"Duplicate entry found for {google_details.name} on {google_details.date}.")
            
        try:
            row = [google_details.date, google_details.name, google_details.work_done]
            google_details._sheet.append_row(row)
            print("Entry added successfully.")
        except Exception as e:
            print(f"Failed to add entry: {e}")
            raise
