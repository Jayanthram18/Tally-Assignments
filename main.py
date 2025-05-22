from workLog.google import GoogleSheetLogger
from datetime import datetime

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️ Input cannot be empty.")

def main():
    try:
        logger = GoogleSheetLogger(sheet_name="SLM_Work_Log", creds_path="credentials.json")
        logger.connect()

        logger.date = datetime.now().strftime("%Y-%m-%d")
        logger.name = get_input("Enter your name: ")
        logger.work_done = get_input("Enter work done: ")

        logger.log_entry()

    except Exception as e:
        print(f" Program failed: {e}")

if __name__ == "__main__":
    main()
