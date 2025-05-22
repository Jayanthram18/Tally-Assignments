import gspread
from oauth2client.service_account import ServiceAccountCredentials
from .base import BaseLogger

class GoogleSheetLogger(BaseLogger):
    def __init__(self, sheet_name, creds_path):
        super().__init__()
        self._sheet_name = sheet_name
        self._creds_path = creds_path
        self._sheet = None

    def connect(self):
        try:
            scope = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]
            creds = ServiceAccountCredentials.from_json_keyfile_name(self._creds_path, scope)
            client = gspread.authorize(creds)
            self._sheet = client.open(self._sheet_name).sheet1
            print(f"Connected to Google Sheet: {self._sheet_name}")
        except Exception as e:
            print(f"Connection Error: {e}")
            raise

    def log_entry(self):
        try:
            if not self._sheet:
                raise Exception("Sheet not connected.")
            row = [self.date, self.name, self.work_done]
            self._sheet.append_row(row)
            print("Entry logged successfully.")
        except Exception as e:
            print(f"Failed to log entry: {e}")
