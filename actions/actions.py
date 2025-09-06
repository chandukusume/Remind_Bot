# actions/actions.py

import pytz
from typing import Any, Text, Dict, List
from datetime import datetime, timedelta
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ReminderScheduled, FollowupAction, SlotSet

# THIS IS THE CORRECT, RELATIVE IMPORT
from . import utils

LOG_FILE = os.path.join(os.path.dirname(__file__), "reminder.log")

def log_message(message: str):
    """Helper function to write a timestamped message to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

# A list of authorized user IDs (e.g., from Telegram, Slack, etc.)
ALLOWED_USERS = ['1301082863'] 

class ActionTrackForm(Action):
    def name(self) -> Text:
        return "action_track_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sender_id = tracker.sender_id
        if sender_id not in ALLOWED_USERS:
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        sheet_id = next(tracker.get_latest_entity_values("sheet_id"), None)
        
        if not sheet_id:
            dispatcher.utter_message(text="Please provide a valid Google Sheet ID to track.")
            return []

        dispatcher.utter_message(text=f"Okay, I am now tracking the form with sheet ID: {sheet_id}")
        return [SlotSet("sheet_id", sheet_id)]


class ActionGetCount(Action):
    def name(self) -> str:
        return "action_get_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        sheet_id = tracker.get_slot("sheet_id")
        if not sheet_id:
            dispatcher.utter_message(text="No form is currently being tracked. Please set one first.")
            return []

        try:
            # You must now call the function with `utils.`
            stats = utils.get_submission_stats(sheet_id) 
            dispatcher.utter_message(
                text=f"📊 Currently, {stats['filled_count']} out of {stats['total_count']} have filled the form."
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
            # You must now call the function with `utils.`
            result_message = utils.send_telegram_reminder(sheet_id)
            dispatcher.utter_message(text=result_message)

            tz = pytz.timezone("Asia/Kolkata")
            trigger_time = datetime.now(tz) + timedelta(minutes=10)
            
            reminder = ReminderScheduled(
                "action_form_reminder",
                trigger_date_time=trigger_time,
                name="form_reminder_scheduler",
                kill_on_user_message=False,
            )
            
            dispatcher.utter_message(text=f"I will send another automatic reminder at {trigger_time.strftime('%I:%M %p')}.")
            return [reminder]

        except Exception as e:
            dispatcher.utter_message(text=f"Failed to send or schedule reminders: {e}")
            return []
            
class ActionFormReminder(Action):
    def name(self) -> str:
        return "action_form_reminder"

    def run(self, dispatcher, tracker, domain):
        return [FollowupAction("action_send_reminder")]


class ActionCheckCurrentForm(Action):
    def name(self) -> str:
        return "action_check_current_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sheet_id = tracker.get_slot("sheet_id")
        
        if sheet_id:
            dispatcher.utter_message(text=f"Currently tracking sheet ID: {sheet_id}.")
        else:
            dispatcher.utter_message(text="No form or sheet is currently being tracked.")
            
        return []