import asyncio
import os
import pytz
import sys
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ReminderScheduled, ReminderCancelled
from datetime import datetime, timedelta
from rasa_sdk.events import FollowupAction


# print("Config exists:", os.path.exists(r"C:\Users\chand\rasa\rasa_env\rasa_files\config.json"))



# Add actions directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import get_count, send_reminder

# Define the path to config.json
CONFIG_PATH = r'C:\Users\chand\rasa\rasa_env\rasa_files\config.json'


class ActionTrackForm(Action):
    def name(self):
        return "action_track_form"

    def run(self, dispatcher, tracker: Tracker, domain):
        print("ActionTrackForm: Starting...")
        sender_id = tracker.sender_id
        allowed_users = ['1301082863']  # Replace with faculty Telegram user IDs
        if sender_id not in allowed_users:
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        entities = tracker.latest_message.get('entities', [])
        sheet_id_entity = next((e for e in entities if e['entity'] == 'sheet_id'), None)
        if sheet_id_entity:
            sheet_id = sheet_id_entity['value']
            try:
                if not os.path.exists(CONFIG_PATH):
                    dispatcher.utter_message(text="Configuration file not found. Please contact the administrator.")
                    return []

                # load config safely
                with open(CONFIG_PATH, 'r') as f:
                    config = json.load(f)

                # update only what we need
                config['current_sheet_id'] = sheet_id
                config['current_form_id'] = None  

                # 🔑 preserve master_sheet_id if it exists
                if 'master_sheet_id' not in config or not config['master_sheet_id']:
                    config['master_sheet_id'] = "1EhkxLV0MrYRzeJAGQOOCuxTMUR0g-QZ0ygy0w44w7AA"

                with open(CONFIG_PATH, 'w') as f:
                    json.dump(config, f, indent=2)

                dispatcher.utter_message(text=f"Now tracking the form with sheet ID {sheet_id}.")
            except Exception as e:
                dispatcher.utter_message(text=f"Failed to set tracking: {str(e)}. Please try again.")
        else:
            dispatcher.utter_message(text="Please provide the sheet ID.")
        return []


class ActionGetCount(Action):
    def name(self):
        return "action_get_count"

    def run(self, dispatcher, tracker: Tracker, domain):
        print("ActionGetCount: Starting...")
        try:
            if not os.path.exists(CONFIG_PATH):
                dispatcher.utter_message(text="Configuration file not found. Please contact the administrator.")
                return []

            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
            sheet_id = config.get('current_sheet_id')
            if sheet_id:
                count = get_count(sheet_id)
                if isinstance(count, str):
                    dispatcher.utter_message(text=count)
                else:
                    dispatcher.utter_message(text=f"Currently, {count} out of 26 have filled the form.")
            else:
                dispatcher.utter_message(text="No form or sheet is currently being tracked.")
        except FileNotFoundError:
            dispatcher.utter_message(text="Configuration file not found. Please contact the administrator.")
        except json.JSONDecodeError:
            dispatcher.utter_message(text="Invalid configuration file format. Please contact the administrator.")
        except PermissionError:
            dispatcher.utter_message(text="Permission denied accessing configuration file.")
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to get the count: {str(e)}. Please try again later.")
        return []


class ActionSendReminder(Action):
    def name(self):
        return "action_send_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        log_path = os.path.join(os.path.dirname(__file__), "reminder.log")

        def log(msg):
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] {msg}\n")

        try:
            log(f"Triggered by sender {tracker.sender_id}")

            if not os.path.exists(CONFIG_PATH):
                msg = "Configuration file not found."
                dispatcher.utter_message(text=msg)
                log(f"ERROR: {msg}")
                return []

            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                config = json.load(f)

            sheet_id = config.get("current_sheet_id")
            if not sheet_id:
                msg = "No form or sheet is currently being tracked."
                dispatcher.utter_message(text=msg)
                log(f"WARNING: {msg}")
                return []

            try:
                count = get_count(sheet_id)
            except Exception as e:
                dispatcher.utter_message(text=f"Error getting count: {e}")
                log(f"EXCEPTION in get_count: {e}")
                return []

            try:
                result = send_reminder(sheet_id)
                dispatcher.utter_message(text=result)
                log(f"Reminder sent: {result}")
            except Exception as e:
                dispatcher.utter_message(text=f"Error sending reminder: {e}")
                log(f"EXCEPTION in send_reminder: {e}")
                return []

            tz = pytz.timezone("Asia/Kolkata")
            reminder_time = (datetime.now(tz) + timedelta(minutes=10, seconds=30)).astimezone(pytz.UTC)

            reminder_name = f"form_reminder_{int(datetime.now().timestamp())}"

            ist_time = reminder_time.astimezone(pytz.timezone("Asia/Kolkata"))  
            log(f"Next reminder scheduled at {reminder_time.isoformat()} UTC / {ist_time.strftime('%Y-%m-%d %H:%M:%S %Z')} IST (name={reminder_name})")

            events = [
                ReminderScheduled(
                    "EXTERNAL_form_reminder",
                    trigger_date_time=reminder_time,
                    name=reminder_name,
                    kill_on_user_message=False
                ),
            ]
            # log(f"Next reminder scheduled at {reminder_time.isoformat()} UTC (name={reminder_name})")
            return events

        except Exception as e:
            dispatcher.utter_message(text=f"Unexpected failure: {e}")
            log(f"UNCAUGHT EXCEPTION: {e}")
            return []
        
class ActionFormReminder(Action):
    def name(self):
        return "action_form_reminder"

    def run(self, dispatcher, tracker, domain):
        return [FollowupAction("action_send_reminder")]


class ActionCheckCurrentForm(Action):
    def name(self):
        return "action_check_current_form"

    def run(self, dispatcher, tracker: Tracker, domain):
        print("ActionCheckCurrentForm: Starting...")
        try:
            if not os.path.exists(CONFIG_PATH):
                dispatcher.utter_message(text="Configuration file not found. Please contact the administrator.")
                return []

            with open(CONFIG_PATH, 'r') as f:
                config = json.load(f)
            form_id = config.get('current_form_id')
            sheet_id = config.get('current_sheet_id')
            if form_id or sheet_id:
                dispatcher.utter_message(text=f"Currently tracking form ID: {form_id or 'Not set'}, sheet ID: {sheet_id or 'Not set'}.")
            else:
                dispatcher.utter_message(text="No form or sheet is currently being tracked.")
        except FileNotFoundError:
            dispatcher.utter_message(text="Configuration file not found. Please contact the administrator.")
        except json.JSONDecodeError:
            dispatcher.utter_message(text="Invalid configuration file format. Please contact the administrator.")
        except PermissionError:
            dispatcher.utter_message(text="Permission denied accessing configuration file.")
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to check current form: {str(e)}.")
        return []