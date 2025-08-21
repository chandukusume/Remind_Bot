from utils import send_reminder
import json
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz  # ✅ use pytz for timezone support

# Load config
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    sheet_id = config.get('current_sheet_id')
except Exception as e:
    print(f"Error loading config: {str(e)}")
    sheet_id = None

# Scheduler
scheduler = BlockingScheduler()

# Example function to update config or run checks
def update_config():
    global sheet_id
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        sheet_id = config.get('current_sheet_id')
        print(f"[Scheduler] Config updated. Current sheet_id: {sheet_id}")
    except Exception as e:
        print(f"[Scheduler] Error updating config: {str(e)}")

# ✅ Fixed: use pytz timezone
scheduler.add_job(update_config, 'interval', minutes=60, timezone=pytz.timezone("Asia/Kolkata"))

if __name__ == "__main__":
    print("[Scheduler] Starting form detector...")
    update_config()  # Run immediately on start
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("[Scheduler] Stopped.")
