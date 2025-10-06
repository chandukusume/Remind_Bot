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
    tz = pytz.timezone("Asia/Kolkata")
    now_ist = tz.localize(datetime.now().replace(tzinfo=None))
    timestamp = now_ist.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_entry = f"[{timestamp}] {message}"
    
    # Always print to console for debugging
    print(f"LOG: {log_entry}")
    
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{log_entry}\n")
            f.flush()  # Force write to disk
    except Exception as e:
        print(f"Failed to write to log file: {e}")

# ✅ INSERT THIS RIGHT AFTER `log_message` is defined
log_message("✅ ACTION SERVER: Fresh code loaded")

# A list of authorized user IDs (e.g., from Telegram, Slack, etc.)
ALLOWED_USERS = ['1301082863'] 

class ActionTrackForm(Action):
    def name(self) -> Text:
        return "action_track_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sender_id = tracker.sender_id
        log_message(f"ActionTrackForm triggered by sender {sender_id}")

        if sender_id not in ALLOWED_USERS:
            log_message(f"Unauthorized access attempt by {sender_id}")
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        sheet_id = next(tracker.get_latest_entity_values("sheet_id"), None)
        log_message(f"Extracted sheet_id: {sheet_id}")
        if not sheet_id:
            log_message("No sheet_id provided")

            dispatcher.utter_message(text="Please provide a valid Google Sheet ID to track.")
            return []
        log_message(f"Setting sheet_id slot to: {sheet_id}")
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
            # All code inside the 'try' block must be indented like this
            result_message = utils.send_telegram_reminder(sheet_id)
            dispatcher.utter_message(text=result_message)
            log_message(f"Reminder sent: {result_message}")
            
            # Use pure pytz UTC for APScheduler compatibility
            utc_tz = pytz.UTC
            utc_now = datetime.now(utc_tz)
            trigger_time_utc = utc_now + timedelta(minutes=10, seconds=30)
            
            # Convert to IST for display
            ist_tz = pytz.timezone("Asia/Kolkata")
            trigger_time_ist = trigger_time_utc.astimezone(ist_tz)
              
            # Create unique reminder name using timestamp
            unique_name = f"form_reminder_{int(trigger_time_utc.timestamp())}"
            
            reminder = ReminderScheduled(
                "form_reminder",
                # Use the UTC time for the scheduler
                trigger_date_time=trigger_time_utc,
                name=unique_name,
                kill_on_user_message=False,
            )
            
            # Use the IST time for the user-facing message
            next_reminder_msg = f"I will send another automatic reminder at {trigger_time_ist.strftime('%I:%M %p')} IST."
            dispatcher.utter_message(text=next_reminder_msg)

            # Use the IST time for the log message
            log_message(f"Next reminder scheduled at {trigger_time_ist.strftime('%Y-%m-%d %H:%M:%S')} IST (name={unique_name})")
            return [reminder]

        except Exception as e:
            # The 'except' must line up with the 'try'
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
        
        # Get sheet_id from slot to ensure continuity
        sheet_id = tracker.get_slot("sheet_id")
        if not sheet_id:
            log_message("Automatic reminder stopped: No form being tracked")
            return []
            
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
