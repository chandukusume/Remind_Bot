# actions/config.py

import os
import sys

def get_env_variable(var_name: str) -> str:
    """Gets an environment variable or exits the program if it's not found."""
    value = os.environ.get(var_name)
    if value is None:
        print(f"CRITICAL ERROR: The environment variable '{var_name}' is not set. The action server cannot start.")
        sys.exit(1)
    return value

# --- Telegram Bot Credentials ---
TELEGRAM_BOT_TOKEN = get_env_variable("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = get_env_variable("TELEGRAM_CHAT_ID")

# --- Google Configuration ---
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "credentials.json")

# MODIFIED: Master Sheet ID is now optional and can be None
MASTER_SHEET_ID = os.environ.get("MASTER_SHEET_ID", None)

# Google API Scopes
GOOGLE_API_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/forms'
]

# --- Database Configuration ---
DB_HOST = get_env_variable("DB_HOST")
DB_NAME = get_env_variable("DB_NAME")
DB_USER = get_env_variable("DB_USER")
DB_PASSWORD = get_env_variable("DB_PASSWORD")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))