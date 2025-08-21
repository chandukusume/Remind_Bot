import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import requests
import json

# Google API configuration
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/forms']
creds = Credentials.from_service_account_file(r'C:\Users\chand\rasa\rasa_env\rasa_files\credentials.json', scopes=scope)
sheets_client = gspread.authorize(creds)
forms_service = build('forms', 'v1', credentials=creds)

# Telegram configuration
bot_token = '8205206073:AAHV-d3ikOEm6Wy6K7zHXGw3ysbtU6skuog'  # Replace with your Telegram bot token
chat_id = '-4781374828'  # Replace with your Telegram group chat ID

def get_count(sheet_id):
    """Get the number of form submissions."""
    if not sheet_id:
        return "No form is currently being tracked."
    try:
        spreadsheet = sheets_client.open_by_key(sheet_id)
        sheet = spreadsheet.sheet1
        records = sheet.get_all_records()
        return len(records)
    except Exception as e:
        return f"Error getting count: {str(e)}"
    
def get_not_filled_students(master_sheet_id, form_sheet_id):
    """Compare master sheet (all students) with form responses and return missing roll numbers."""
    try:
        # Load master sheet (expects Roll, Name headers)
        master_sheet = sheets_client.open_by_key(master_sheet_id).sheet1
        master_records = master_sheet.get_all_records()

        # Load form responses sheet (expects Roll column at least)
        form_sheet = sheets_client.open_by_key(form_sheet_id).sheet1
        form_records = form_sheet.get_all_records()

        # Extract rolls
        master_rolls = {str(row["Roll"]): row["Name"] for row in master_records if "Roll" in row and "Name" in row}
        filled_rolls = {str(row["Roll"]) for row in form_records if "Roll" in row}

        # Find missing
        missing = {roll: name for roll, name in master_rolls.items() if roll not in filled_rolls}
        # total count
        total_count = len(master_rolls)
        filled_count = len(filled_rolls)
        return missing, filled_count, total_count

    except Exception as e:
        return f"Error fetching missing students: {e}"
    
def send_reminder(sheet_id):
    """Send Telegram reminder with missing students list."""
    if not sheet_id:
        return "No form is currently being tracked."
    try:
        # Load config to get master sheet
        with open(r'C:\Users\chand\rasa\rasa_env\rasa_files\config.json', "r", encoding="utf-8") as f:
            config = json.load(f)
        print("DEBUG - Loaded config:", config)   # <--- add this line
        master_sheet_id = config.get("master_sheet_id")
        print("DEBUG - master_sheet_id:", master_sheet_id)  # <--- and this


        if not master_sheet_id:
            return "Master sheet not configured."

        # Get missing students
        result = get_not_filled_students(master_sheet_id, sheet_id)
        if isinstance(result, str):  # error string
            return result
        
        missing, filled_count, total_count = result

        if not missing:
            message = f"✅ All {total_count} students have filled the form."
        else:
            message_lines = [f"📊 {filled_count} out of {total_count} students have filled the form."]
            message_lines.append("\n⚠️ The following students have not filled the form:")
            for roll, name in missing.items():
                message_lines.append(f"{roll} - {name}")
            message = "\n".join(message_lines)

        # Send message to Telegram
        url = f"https://api.telegram.org/bot8205206073:AAHV-d3ikOEm6Wy6K7zHXGw3ysbtU6skuog/sendMessage"
        payload = {"chat_id": chat_id, "text": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return "Reminder sent with missing students list."
        else:
            return f"Failed to send reminder: {response.text}"

    except Exception as e:
        return f"Error sending reminder: {str(e)}"

def get_linked_sheet_id(form_id):
    """Retrieve the linked Google Sheet ID for a form."""
    try:
        form = forms_service.forms().get(formId=form_id).execute()
        linked_sheet_id = form.get('linkedSheetId')
        if not linked_sheet_id:
            return None, "No linked sheet found for this form."
        return linked_sheet_id, None
    except Exception as e:
        return None, f"Error retrieving linked sheet: {str(e)}"

def check_new_forms(last_known_form_id=None):
    """Check for new forms and return the latest form ID and sheet ID."""
    try:
        forms = forms_service.forms().list().execute().get('forms', [])
        if not forms:
            return None, None, "No forms found."
        # Sort by title (proxy for newest form)
        forms.sort(key=lambda x: x.get('info', {}).get('documentTitle', ''), reverse=True)
        latest_form = forms[0]
        form_id = latest_form['formId']
        if last_known_form_id and form_id == last_known_form_id:
            return None, None, "No new forms detected."
        sheet_id, error = get_linked_sheet_id(form_id)
        if error:
            return form_id, None, error
        return form_id, sheet_id, None
    except Exception as e:
        return None, None, f"Error checking forms: {str(e)}"
if __name__ == "__main__":
    test_sheet = "1r8H8w36dc9vY5c4IZcNxn-qnNSqzPZHor_AEjbk2yzE"
    print(send_reminder(test_sheet))
    
