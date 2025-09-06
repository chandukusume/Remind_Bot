import asyncio
import os
import pytz
import sys
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ReminderScheduled, ReminderCancelled
from datetime import datetime, timedelta
from rasa_sdk.events import SlotSet
from rasa_sdk.events import FollowupAction
from . import utils


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
    def name(self) -> str:
        return "action_get_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        sheet_id = tracker.get_slot("sheet_id")
        if not sheet_id:
            dispatcher.utter_message(text="No form is currently being tracked. Please set one first.")
            return []

        try:
            # Call the new, more detailed utility function
            stats = utils.get_submission_stats(sheet_id)
            dispatcher.utter_message(
                text=f"Currently, {stats['filled_count']} out of {stats['total_count']} have filled the form."
            )
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to get the count: {e}")
            
        return []


class ActionSendReminder(Action):
    def name(self) -> str:
        return "action_send_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        sheet_id = tracker.get_slot("sheet_id")
        if not sheet_id:
            dispatcher.utter_message(text="I can't send reminders because no form is being tracked.")
            return []

        try:
            # The new utility function handles everything and returns a simple success message
            result_message = utils.send_telegram_reminder(sheet_id)
            dispatcher.utter_message(text=result_message)
        except Exception as e:
            dispatcher.utter_message(text=f"Failed to send reminder: {e}")
            
        # You can add back the scheduling logic here if you want a recurring reminder
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