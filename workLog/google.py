import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .base import BaseLogger

class GoogleSheetLogger(BaseLogger):
    def __init__(self, sheet_name, creds_path):
        self.sheet_name = sheet_name
        self.creds_path = creds_path
        self.sheet = None

    def connect(self):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.creds_path, scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(self.sheet_name).sheet1
        print("Connected to Google Sheet.")

    def log_entry(self, date, name, work_done):
        if not self.sheet:
            raise Exception("Sheet is not connected.")
        
        row = [date, name, work_done]
        self.sheet.append_row(row)
        print("Entry added successfully.")
