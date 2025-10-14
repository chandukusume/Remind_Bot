# actions/actions.py

import os
import pytz
from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ReminderScheduled, ReminderCancelled, FollowupAction, SlotSet
from rasa_sdk.forms import FormValidationAction

# This imports the helper functions from your utils.py
from . import utils
# This imports the configuration variables from your config.py
from . import config
from . import database

LOG_FILE = os.path.join(os.path.dirname(__file__), "reminder.log")

def log_message(message: str):
    """Helper function to write a timestamped message to the log file."""
    tz = pytz.timezone("Asia/Kolkata")
    now_ist = datetime.now(tz)
    timestamp = now_ist.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    log_entry = f"[{timestamp}] {message}"
    
    print(f"LOG: {log_entry}") # Always print to console for debugging
    
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{log_entry}\n")
            f.flush()
    except Exception as e:
        print(f"Failed to write to log file: {e}")

log_message("✅ ACTION SERVER: Fresh code loaded")

# A list of authorized user IDs from Telegram
ALLOWED_USERS = ['1301082863'] 

def is_authorized(tracker: Tracker) -> bool:
    """Check if the sender is in the allowed users list."""
    sender_id = tracker.sender_id
    if sender_id not in ALLOWED_USERS:
        log_message(f"Unauthorized access attempt by {sender_id}")
        return False
    return True

# --- ACTIONS FOR CONFIGURATION ---

class ActionSetMasterSheet(Action):
    def name(self) -> Text:
        return "action_set_master_sheet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        sheet_id = tracker.get_slot("master_sheet_id")
        database.save_master_sheet_id(sheet_id)
        log_message(f"Successfully set and validated master_sheet_id slot to: {sheet_id}")
        dispatcher.utter_message(text=f"Okay, I have set the master sheet ID to: {sheet_id}")
        return []

class ActionSetActiveSheet(Action):
    def name(self) -> Text:
        return "action_set_active_sheet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        sheet_id = tracker.get_slot("active_sheet_id")
        database.save_active_sheet_id(sheet_id)
        log_message(f"Successfully set active_sheet_id slot to: {sheet_id}")
        dispatcher.utter_message(text=f"Okay, I am now focused on the sheet with ID: {sheet_id}")
        return []

class ActionSetScheduleTime(Action):
    def name(self) -> Text:
        return "action_set_schedule_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        schedule_time = tracker.get_slot("schedule_time")
        log_message(f"Successfully set schedule_time slot to: {schedule_time}")
        dispatcher.utter_message(text=f"Okay, I have set the schedule time to: {schedule_time}")
        return []

class ActionUnsetScheduleTime(Action):
    def name(self) -> Text:
        return "action_unset_schedule_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        log_message("Schedule time has been cleared")
        dispatcher.utter_message(text="✅ Schedule time has been cleared. Default interval will be used for reminders.")
        return [SlotSet("schedule_time", None)]

class ActionUnsetMasterSheet(Action):
    def name(self) -> Text:
        return "action_unset_master_sheet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        database.save_master_sheet_id(None)
        log_message("Master sheet has been cleared")
        dispatcher.utter_message(text="✅ Master sheet has been cleared.")
        return [SlotSet("master_sheet_id", None)]

class ActionUnsetActiveSheet(Action):
    def name(self) -> Text:
        return "action_unset_active_sheet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        database.save_active_sheet_id(None)
        log_message("Active sheet has been cleared")
        dispatcher.utter_message(text="✅ Active sheet has been cleared.")
        return [SlotSet("active_sheet_id", None)]

class ActionCancel(Action):
    def name(self) -> Text:
        return "action_cancel"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        log_message("User cancelled current operation")
        dispatcher.utter_message(text="✅ Operation cancelled. How can I help you?")
        return []

# --- ACTIONS FOR GETTING INFORMATION ---

class ActionCheckActiveSheet(Action):
    def name(self) -> str:
        return "action_check_active_sheet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        active_sheet_id = tracker.get_slot("active_sheet_id") or database.get_active_sheet_id()
        if active_sheet_id:
            dispatcher.utter_message(response="utter_check_active_sheet", active_sheet_id=active_sheet_id)
        else:
            dispatcher.utter_message(response="utter_no_active_sheet")
        return []

class ActionGetCount(Action):
    def name(self) -> str:
        return "action_get_count"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        active_sheet_id = tracker.get_slot("active_sheet_id") or database.get_active_sheet_id()
        if not active_sheet_id:
            dispatcher.utter_message(response="utter_no_active_sheet")
            return []

        master_id_from_slot = tracker.get_slot("master_sheet_id") or database.get_master_sheet_id()
        if not master_id_from_slot:
            dispatcher.utter_message(text="The Master Sheet ID has not been set yet. Please set it first using the '/set_master_sheet' command.")
            return []

        try:
            log_message(f"Getting count for active sheet '{active_sheet_id}' using master sheet '{master_id_from_slot}'")
            stats = utils.get_submission_stats(active_sheet_id, master_id_from_slot) 
            message = f"📊 Currently, {stats['filled_count']} out of {stats['total_count']} have filled the form."
            dispatcher.utter_message(text=message)
        except Exception as e:
            error_msg = f"Sorry, I failed to get the count: {e}"
            dispatcher.utter_message(text=error_msg)
            log_message(f"ERROR getting count: {e}")
        return []

class ActionShowInfo(Action):
    def name(self) -> str:
        return "action_show_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        master_sheet_id = tracker.get_slot("master_sheet_id") or database.get_master_sheet_id()
        active_sheet_id = tracker.get_slot("active_sheet_id") or database.get_active_sheet_id()
        schedule_time = tracker.get_slot("schedule_time")
        
        # Get sheet names instead of IDs
        master_sheet_name = utils.get_sheet_name(master_sheet_id) if master_sheet_id else 'Not set'
        active_sheet_name = utils.get_sheet_name(active_sheet_id) if active_sheet_id else 'Not set'
        
        info_message = "📋 Current Configuration:\n\n"
        info_message += f"🗂️ Master Sheet: {master_sheet_name}\n"
        info_message += f"📊 Active Sheet: {active_sheet_name}\n"
        info_message += f"⏰ Schedule Time: {schedule_time or 'Not set'}\n"
        
        dispatcher.utter_message(text=info_message)
        return []

# --- ACTIONS FOR REMINDERS ---

class ActionSendReminder(Action):
    def name(self) -> str:
        return "action_send_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []

        active_sheet_id = tracker.get_slot("active_sheet_id") or database.get_active_sheet_id()
        if not active_sheet_id:
            dispatcher.utter_message(response="utter_no_active_sheet")
            return []

        master_id_from_slot = tracker.get_slot("master_sheet_id") or database.get_master_sheet_id()
        if not master_id_from_slot:
            dispatcher.utter_message(text="The Master Sheet ID has not been set. Please set it first.")
            return []
        
        recipient_group = tracker.get_slot("recipient_group") or "everyone"

        try:
            # Send immediate reminder
            log_message(f"Sending immediate reminder for active sheet '{active_sheet_id}' using master sheet '{master_id_from_slot}'")
            result_message = utils.send_telegram_reminder(active_sheet_id, recipient_group, master_id_from_slot)
            dispatcher.utter_message(text=result_message)
            
            # Start recurring reminders
            schedule_time = tracker.get_slot("schedule_time") or "5 minutes"
            schedule_lower = schedule_time.lower()
            numbers = ''.join(filter(str.isdigit, schedule_time))
            num = int(numbers) if numbers else 5
            
            if any(word in schedule_lower for word in ['minute', 'min', 'm']):
                interval = timedelta(minutes=num)
            elif any(word in schedule_lower for word in ['hour', 'hr', 'h']):
                interval = timedelta(hours=num)
            elif any(word in schedule_lower for word in ['second', 'sec', 's']):
                interval = timedelta(seconds=num)
            else:
                interval = timedelta(minutes=num)
                
            trigger_time = datetime.now(pytz.UTC) + interval
            reminder = ReminderScheduled(
                "action_handle_scheduled_reminder", 
                trigger_date_time=trigger_time, 
                name="recurring_reminder_job", 
                kill_on_user_message=False
            )
            
            ist_tz = pytz.timezone('Asia/Kolkata')
            trigger_time_ist = trigger_time.astimezone(ist_tz)
            dispatcher.utter_message(text=f"✅ Recurring reminders activated! Next reminder at {trigger_time_ist.strftime('%H:%M:%S')} IST")
            log_message(f"✅ SCHEDULED: Recurring reminder started with interval: {interval}")
            
            return [reminder, SlotSet("recipient_group", None)]
            
        except Exception as e:
            error_msg = f"Failed to send reminders: {e}"
            dispatcher.utter_message(text=error_msg)
            log_message(f"ERROR sending reminder: {e}")
            return []

class ActionScheduleReminder(Action):
    def name(self) -> str:
        return "action_schedule_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []
        
        log_message("ActionScheduleReminder triggered")
        
        # Check if required sheets are set
        active_sheet_slot = tracker.get_slot("active_sheet_id")
        master_sheet_slot = tracker.get_slot("master_sheet_id")
        
        log_message(f"Slots - Active: {active_sheet_slot}, Master: {master_sheet_slot}")
        
        try:
            active_sheet_db = database.get_active_sheet_id()
            master_sheet_db = database.get_master_sheet_id()
            log_message(f"Database - Active: {active_sheet_db}, Master: {master_sheet_db}")
        except Exception as e:
            log_message(f"Database error: {e}")
            active_sheet_db = None
            master_sheet_db = None
        
        active_sheet_id = active_sheet_slot or active_sheet_db
        master_sheet_id = master_sheet_slot or master_sheet_db
        
        log_message(f"Final values - Active: {active_sheet_id}, Master: {master_sheet_id}")
        
        if not active_sheet_id:
            dispatcher.utter_message(text="❌ Please set an active sheet first using /set_active_sheet")
            log_message("ERROR: No active sheet ID found")
            return []
            
        if not master_sheet_id:
            dispatcher.utter_message(text="❌ Please set a master sheet first using /set_master_sheet")
            log_message("ERROR: No master sheet ID found")
            return []
            
        # Get schedule time from slot or use default interval
        schedule_time = tracker.get_slot("schedule_time") or "5 minutes"
        log_message(f"Using schedule time: {schedule_time}")
        
        # Parse interval with better format support
        schedule_lower = schedule_time.lower()
        numbers = ''.join(filter(str.isdigit, schedule_time))
        num = int(numbers) if numbers else 5
        
        if any(word in schedule_lower for word in ['minute', 'min', 'm']):
            interval = timedelta(minutes=num)
        elif any(word in schedule_lower for word in ['hour', 'hr', 'h']):
            interval = timedelta(hours=num)
        elif any(word in schedule_lower for word in ['second', 'sec', 's']):
            interval = timedelta(seconds=num)
        else:
            interval = timedelta(minutes=num)  # default to minutes
            
        trigger_time = datetime.now(pytz.UTC) + interval
        reminder = ReminderScheduled(
            "action_handle_scheduled_reminder", 
            trigger_date_time=trigger_time, 
            name="recurring_reminder_job", 
            kill_on_user_message=False
        )
        
        # Convert UTC to IST for display
        ist_tz = pytz.timezone('Asia/Kolkata')
        trigger_time_ist = trigger_time.astimezone(ist_tz)
        dispatcher.utter_message(text=f"✅ Reminders started! Sending every {schedule_time}. Next reminder at {trigger_time_ist.strftime('%H:%M:%S')} IST")
        log_message(f"✅ SCHEDULED: Recurring reminder with interval: {interval}, next trigger: {trigger_time.isoformat()}")
        
        # Clear slots to prevent conversation pollution
        return [
            reminder,
            SlotSet("recipient_group", None)
        ]

class ActionHandleScheduledReminder(Action):
    def name(self) -> str:
        return "action_handle_scheduled_reminder"

    def run(self, dispatcher, tracker, domain):
        log_message("Automatic reminder triggered by scheduler.")
        
        # Send the reminder
        active_sheet_id = tracker.get_slot("active_sheet_id") or database.get_active_sheet_id()
        master_id = tracker.get_slot("master_sheet_id") or database.get_master_sheet_id()
        
        if active_sheet_id and master_id:
            try:
                result_message = utils.send_telegram_reminder(active_sheet_id, "everyone", master_id)
                log_message(f"Scheduled reminder sent: {result_message}")
            except Exception as e:
                log_message(f"ERROR in scheduled reminder: {e}")
        
        # Schedule the next reminder
        schedule_time = tracker.get_slot("schedule_time") or "5 minutes"
        
        schedule_lower = schedule_time.lower()
        numbers = ''.join(filter(str.isdigit, schedule_time))
        num = int(numbers) if numbers else 5
        
        if any(word in schedule_lower for word in ['minute', 'min', 'm']):
            interval = timedelta(minutes=num)
        elif any(word in schedule_lower for word in ['hour', 'hr', 'h']):
            interval = timedelta(hours=num)
        elif any(word in schedule_lower for word in ['second', 'sec', 's']):
            interval = timedelta(seconds=num)
        else:
            interval = timedelta(minutes=num)
            
        next_trigger = datetime.now(pytz.UTC) + interval
        next_reminder = ReminderScheduled(
            "action_handle_scheduled_reminder", 
            trigger_date_time=next_trigger, 
            name="recurring_reminder_job", 
            kill_on_user_message=False
        )
        
        log_message(f"Next reminder scheduled for: {next_trigger.isoformat()}")
        
        # Clear conversation slots to prevent memory pollution
        return [
            next_reminder,
            SlotSet("recipient_group", None)
        ]

class ActionStopReminder(Action):
    def name(self) -> str:
        return "action_stop_reminder"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []
        dispatcher.utter_message(response="utter_reminders_stopped")
        log_message("User requested to stop all reminders.")
        return [ReminderCancelled()]

class ActionRestartReminders(Action):
    def name(self) -> str:
        return "action_restart_reminders"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not is_authorized(tracker):
            dispatcher.utter_message(text="You are not authorized to perform this action.")
            return []
        dispatcher.utter_message(response="utter_reminders_restarted")
        log_message("User requested to restart reminders.")
        return [FollowupAction("action_schedule_reminder")]

# --- FORM VALIDATION ACTIONS ---

class ValidateMasterSheetForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_master_sheet_form"

    async def validate_master_sheet_id(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate the master_sheet_id value."""
        log_message(f"Validating master_sheet_id: '{slot_value}'")
        # A real Google Sheet ID is 44 characters long.
        if isinstance(slot_value, str) and len(slot_value) > 40:
            log_message("Validation successful.")
            return {"master_sheet_id": slot_value}
        else:
            log_message("Validation failed: ID is not valid.")
            dispatcher.utter_message(text="That doesn't look like a valid Google Sheet ID. Please try again.")
            return {"master_sheet_id": None}

class ValidateActiveSheetForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_active_sheet_form"

    async def validate_active_sheet_id(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate the active_sheet_id value."""
        log_message(f"Validating active_sheet_id: '{slot_value}'")
        if isinstance(slot_value, str) and len(slot_value) > 10:
            log_message("Active sheet validation successful.")
            return {"active_sheet_id": slot_value}
        else:
            log_message("Active sheet validation failed: ID is not valid.")
            dispatcher.utter_message(text="That doesn't look like a valid Google Sheet ID. Please try again.")
            return {"active_sheet_id": None}

class ValidateTimeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_time_form"
    
    async def validate_schedule_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate schedule_time value."""
        # This is a placeholder. A real implementation would parse the time.
        log_message(f"Validating schedule_time: '{slot_value}'")
        if isinstance(slot_value, str) and len(slot_value) > 3:
             return {"schedule_time": slot_value}
        else:
             dispatcher.utter_message(text="Please provide a valid time or schedule (e.g., 'every Friday at 5pm').")
             return {"schedule_time": None}