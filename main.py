from datetime import date
from workLog.google import GoogleSheetLogger

def main():
    logger = GoogleSheetLogger(
        sheet_name="SLM_Work_Log",
        creds_path="credentials.json"
    )

    logger.connect()

    today = str(date.today())
    name = input("Enter your name: ")
    work_done = input("What did you work on today? ")

    logger.log_entry(today, name, work_done)

if __name__ == "__main__":
    main()
