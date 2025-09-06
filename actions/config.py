# actions/config.py

import os

# --- Configuration for your bot ---

# IMPORTANT: For security, it's best to set these as environment variables
# in your operating system rather than writing them here directly.
# Example: TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Telegram Bot Credentials
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8205206073:AAHV-d3ikOEm6Wy6K7zHXGw3ysbtU6skuog")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "-4781374828")

# Google Service Account Credentials File
# Place your 'credentials.json' file in the root of your Rasa project
SERVICE_ACCOUNT_FILE = os.environ.get("SERVICE_ACCOUNT_FILE", "credentials.json")

# The ID of your master spreadsheet that contains the full list of all students
# It's better to set this as a slot in Rasa if it changes often, or keep it here if it's static.
MASTER_SHEET_ID = os.environ.get("MASTER_SHEET_ID", "1EhkxLV0MrYRzeJAGQOOCuxTMUR0g-QZ0ygy0w44w7AA")

# Google API Scopes
GOOGLE_API_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/forms'
]