from workLog.google import GoogleSheetLogger
from datetime import datetime

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")

def get_valid_date(prompt):
    while True:
        date_input = input(prompt).strip()
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            return date_input
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

def get_valid_field(prompt, setter):
    while True:
        value = get_input(prompt)
        try:
            setter(value)  
            return
        except ValueError as e:
            print(f"{e}")

def main():
    try:
        logger = GoogleSheetLogger(sheet_name="SLM_Work_Log", creds_path="credentials.json")
        logger.connect()

        while True:
            logger.date = get_valid_date("📅 Enter the date (DD-MM-YYYY): ")

            get_valid_field("Enter your name: ", lambda val: setattr(logger, 'name', val))
            get_valid_field("Enter work done: ", lambda val: setattr(logger, 'work_done', val))

            try:
                logger.log_entry()
               
            except Exception as log_err:
                print(f"Failed to log task: {log_err}")

            choice = input("➕ Do you want to log another task? (y/n): ").strip().lower()
            if choice != 'y':
                print("Exiting the logger.")
                break

    except Exception as e:
        print(f"Program failed: {e}")

if __name__ == "__main__":
    main()
