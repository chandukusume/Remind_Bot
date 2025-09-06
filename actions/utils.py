# actions/utils.py

import gspread
import requests
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Import configuration from your new config file
from . import config

# --- Client Initialization ---
# This pattern creates the API clients only when they are first needed.

_sheets_client = None
_forms_service = None

def _get_sheets_client():
    """Initializes and returns the gspread client."""
    global _sheets_client
    if _sheets_client is None:
        creds = Credentials.from_service_account_file(config.SERVICE_ACCOUNT_FILE, scopes=config.GOOGLE_API_SCOPES)
        _sheets_client = gspread.authorize(creds)
    return _sheets_client

def _get_forms_service():
    """Initializes and returns the Google Forms service client."""
    global _forms_service
    if _forms_service is None:
        creds = Credentials.from_service_account_file(config.SERVICE_ACCOUNT_FILE, scopes=config.GOOGLE_API_SCOPES)
        _forms_service = build('forms', 'v1', credentials=creds)
    return _forms_service

# --- Core Logic Functions ---

def get_submission_stats(form_sheet_id: str) -> dict:
    """
    Compares the master sheet with form responses and returns a dictionary of stats.
    Raises exceptions on failure.
    """
    try:
        sheets_client = _get_sheets_client()
        
        # Load master sheet (expects 'Roll' and 'Name' columns)
        master_sheet = sheets_client.open_by_key(config.MASTER_SHEET_ID).sheet1
        master_records = master_sheet.get_all_records()

        # Load form responses sheet (expects a 'Roll' column)
        form_sheet = sheets_client.open_by_key(form_sheet_id).sheet1
        form_records = form_sheet.get_all_records()

        # Extract roll numbers and names
        master_rolls = {str(row["Roll"]): row["Name"] for row in master_records if "Roll" in row and "Name" in row}
        filled_rolls = {str(row["Roll"]) for row in form_records if "Roll" in row}

        # Find who is missing
        missing_students = {roll: name for roll, name in master_rolls.items() if roll not in filled_rolls}
        
        return {
            "missing": missing_students,
            "filled_count": len(filled_rolls),
            "total_count": len(master_rolls)
        }
    except gspread.exceptions.SpreadsheetNotFound:
        raise ValueError("A spreadsheet was not found. Check the Sheet ID and sharing permissions.")
    except KeyError as e:
        raise ValueError(f"A required column is missing in one of the sheets: {e}")
    except Exception as e:
        # Re-raise other exceptions to be handled by the action
        raise e

def send_telegram_reminder(form_sheet_id: str) -> str:
    """
    Constructs and sends a detailed reminder message to a Telegram group.
    """
    if not form_sheet_id:
        raise ValueError("No form sheet ID was provided.")
        
    stats = get_submission_stats(form_sheet_id)
    missing = stats["missing"]
    filled_count = stats["filled_count"]
    total_count = stats["total_count"]

    # Construct the message
    if not missing:
        message = f"✅ All {total_count} students have filled the form. Great job!"
    else:
        message_lines = [f"📊 *Form Submission Status*"]
        message_lines.append(f"{filled_count} out of {total_count} students have responded.")
        message_lines.append("\n⚠️ *The following students have not yet filled the form:*")
        for roll, name in sorted(missing.items()): # Sort by roll number
            message_lines.append(f"`{roll}` - {name}")
        message = "\n".join(message_lines)

    # Send the message to Telegram
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown" # Use Markdown for bolding and code blocks
    }
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return "Reminder sent successfully to the Telegram group."
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to send message to Telegram: {e}")

# --- Google Forms Specific Functions (Optional, but good to have) ---

def get_linked_sheet_id(form_id: str) -> str:
    """Retrieves the linked Google Sheet ID for a given Google Form ID."""
    try:
        forms_service = _get_forms_service()
        form = forms_service.forms().get(formId=form_id).execute()
        linked_sheet_id = form.get('linkedSheetId')
        
        if not linked_sheet_id:
            raise ValueError("No linked sheet found for this form.")
            
        return linked_sheet_id
    except Exception as e:
        raise ConnectionError(f"Error retrieving linked sheet: {e}")