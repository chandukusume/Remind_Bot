# actions/actions.py

import os
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
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            f.write(f"[{timestamp}] {message}\n")
            f.flush()  # Force write to disk
    except Exception as e:
        print(f"Failed to write to log: {e}")  # Fallback to console
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
        sender_id = tracker.sender_id
        log_message(f"Triggered by sender {sender_id}")
        
        sheet_id = tracker.get_slot("sheet_id")
        if not sheet_id:
            dispatcher.utter_message(text="No form is currently being tracked. Please set one first.")
            log_message("Count returned message: No form being tracked")
            return []

        try:
            stats = utils.get_submission_stats(sheet_id) 
            message = f"📊 Currently, {stats['filled_count']} out of {stats['total_count']} have filled the form."
            dispatcher.utter_message(text=message)
            log_message(f"Count returned message: {stats['filled_count']} out of {stats['total_count']} have filled")
        except Exception as e:
            error_msg = f"Failed to get the count: {e}"
            dispatcher.utter_message(text=error_msg)
            log_message(f"Count returned message: Error getting count: {e}")
            
        return []


class ActionSendReminder(Action):
    def name(self) -> str:
        return "action_send_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        sender_id = tracker.sender_id
        log_message(f"Triggered by sender {sender_id}")
        
        sheet_id = tracker.get_slot("sheet_id")
        if not sheet_id:
            dispatcher.utter_message(text="I can't send reminders because no form is being tracked.")
            log_message("Reminder sent: No form being tracked")
            return []

        try:
            result_message = utils.send_telegram_reminder(sheet_id)
            dispatcher.utter_message(text=result_message)
            log_message(f"Reminder sent: {result_message}")

            tz = pytz.timezone("Asia/Kolkata")
            trigger_time = datetime.now(tz) + timedelta(minutes=10)
            
            reminder = ReminderScheduled(
                "action_form_reminder",
                trigger_date_time=trigger_time,
                name="form_reminder_scheduler",
                kill_on_user_message=False,
            )
            
            next_reminder_msg = f"I will send another automatic reminder at {trigger_time.strftime('%I:%M %p')}."
            dispatcher.utter_message(text=next_reminder_msg)
            log_message(f"Next reminder scheduled at {trigger_time.strftime('%Y-%m-%dT%H:%M:%S%z')} (name=form_reminder_scheduler)")
            return [reminder]

        except Exception as e:
            error_msg = f"Failed to send or schedule reminders: {e}"
            dispatcher.utter_message(text=error_msg)
            log_message(f"Reminder sent: Error sending reminder: {e}")
            return []
            
class ActionFormReminder(Action):
    def name(self) -> str:
        return "action_form_reminder"
    def run(self, dispatcher, tracker, domain):
        sender_id = tracker.sender_id
        log_message(f"Automatic reminder triggered for sender {sender_id}")
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

