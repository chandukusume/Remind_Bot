# Remind Bot

Your automated assistant for tracking student submissions, so you don't have to.
* Remind Bot is a rule-based chatbot for faculty that automates the tedious process of tracking student form submissions. Integrated with platforms like Telegram, it sends scheduled reminders to students who haven't submitted, provides real-time completion statistics, and generates lists of non-submitters on command.

![Demo GIF of Remind Bot in action](Suggestion: Add a GIF here showing the bot's commands and responses)

### The Problem: 
* Faculty members spend countless hours manually cross-referencing student lists with form responses, sending follow-up emails, and compiling lists of students who are late. This manual work is repetitive, time-consuming, and prone to errors.

### The Solution :
* Remind Bot acts as a dedicated digital assistant. By connecting to a Google Sheet of responses and a master student list, it takes over the entire tracking and reminding process. This frees up valuable faculty time to focus on teaching and student engagement, not administrative busywork.

## Key Features

* Automated Tracking: Set it up once and let the bot monitor submissions 24/7.
* Scheduled Reminders: Automatically sends reminders to students who have not yet submitted the form at a pre-defined time.
*  Real-Time Stats: Instantly get a count of how many students have submitted the form with a simple command.
* Non-Submitter Lists: Generate and send a clean, formatted list of students who still need to submit.

* Platform Integration: Operates directly within Telegram, where communication is fast and direct.


## How It Works
* Setup: The faculty member registers a Google Form's response sheet and a master student list with the bot.

* Monitor: The bot periodically fetches the list of submitted student IDs from the Google Sheet.

*Compare: It cross-references the submitted list with the master student list to identify who is pending.

*Remind & Report: Based on commands or a schedule, the bot messages the faculty group with reminders, stats, or lists of non-submitters.

## Getting Started

 #### Prerequisites : 
 Python 3.8+

#### A Telegram Bot Token (Get one from BotFather)

#### Google Cloud Platform project with Google Sheets API and Google Drive API enabled.

#### A credentials.json file for your Google Cloud service account.

## Installation

- Clone the repository:

     ```bash
             git clone https://github.com/chandukusume/Remind_Bot.git cd Remind_Bot
     ```
- Install the dependencies:

     ```bash
                pip install foobar   
                pip install -r requirements.txt
     ```
####  Configure environment variables:
- Rename the .env.example file to .env and add your credentials:


#### Code snippet

                 TELEGRAM_BOT_TOKEN='Your_Telegram_Bot_Token_Here'

                 GOOGLE_SHEETS_CREDENTIALS_FILE='path/to/your/credentials.json'

#### Run the bot :
           
   ```bash       
           python main.py
   ```
#### Usage (Bot Commands)

- Once the bot is running and added to your Telegram group, you can use the following commands:

```bash 
/start - Display a welcome message and help information.

/register_form <sheet_url> <student_list_url> - Register a new form to track.

/status - Get the current submission count (e.g., "78/125 students have submitted.").

/list_pending - Receive a list of all students who have not yet submitted.

/set_reminder HH:MM - Set a daily time for automatic reminders (e.g., /set_reminder 16:00).

```

## Technology Stack

- Backend: Python

- Platform: Telegram Bot API

- Data Source: Google Sheets API

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

   ```bash 
Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

   ```
 
##  License

- Distributed under the MIT License. See LICENSE for more information.

