#!/usr/bin/env python3
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = os.getenv("RASA_URL", "http://localhost:5005/webhooks/rest/webhook")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "telegram-bridge"})


@app.route('/webhooks/telegram/webhook', methods=['POST'])
def telegram_webhook():
    print(f"Received webhook: {request.json}")
    data = request.json
    
    # Handle regular messages
    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')
        print(f"Processing message: {text} from chat: {chat_id}")
        
        process_user_input(chat_id, text)
    
    # Handle button clicks (callback queries)
    elif 'callback_query' in data:
        callback_query = data['callback_query']
        chat_id = callback_query['message']['chat']['id']
        callback_data = callback_query['data']
        
        print(f"Processing button click: '{callback_data}' from chat: {chat_id}")
        
        # Answer the callback query to remove loading state
        answer_result = answer_callback_query(callback_query['id'])
        print(f"Callback query answer result: {answer_result}")
        
        # Process the button payload as a message
        print(f"Sending button payload to Rasa: '{callback_data}'")
        process_user_input(chat_id, callback_data)
    
    return jsonify({"status": "ok"})

def process_user_input(chat_id, text):
    """Process user input and send to Rasa"""
    # Send to Rasa
    print(f"Sending to Rasa: {RASA_URL}")
    rasa_response = requests.post(RASA_URL, json={
        "sender": str(chat_id),
        "message": text
    })
    
    print(f"Rasa response status: {rasa_response.status_code}")
    print(f"Rasa response: {rasa_response.text}")
    
    # Send response back to Telegram
    if rasa_response.status_code == 200:
        responses = rasa_response.json()
        print(f"Rasa responses: {responses}")
        for response in responses:
            if 'text' in response:
                # Check if response has buttons
                buttons = response.get('buttons', [])
                if buttons:
                    print(f"Sending to Telegram with buttons: {response['text']}")
                    result = send_telegram_message_with_buttons(chat_id, response['text'], buttons)
                else:
                    print(f"Sending to Telegram: {response['text']}")
                    result = send_telegram_message(chat_id, response['text'])
                print(f"Telegram send result: {result}")

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": chat_id, "text": text})
    return response.status_code, response.text

def send_telegram_message_with_buttons(chat_id, text, buttons):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    # Convert Rasa buttons to Telegram inline keyboard
    keyboard = []
    for button in buttons:
        button_text = button.get('title', button.get('text', 'Button'))
        button_payload = button.get('payload', button.get('title', 'button'))
        
        # Ensure payload starts with / for commands
        if not button_payload.startswith('/'):
            button_payload = f"/{button_payload}"
            
        keyboard.append([{
            "text": button_text,
            "callback_data": button_payload
        }])
        
        print(f"Button created: {button_text} -> {button_payload}")
    
    reply_markup = {
        "inline_keyboard": keyboard
    }
    
    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": reply_markup
    }
    
    print(f"Sending message with keyboard: {payload}")
    response = requests.post(url, json=payload)
    print(f"Telegram API response: {response.status_code} - {response.text}")
    return response.status_code, response.text

def answer_callback_query(callback_query_id):
    """Answer callback query to remove loading state from button"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/answerCallbackQuery"
    response = requests.post(url, json={"callback_query_id": callback_query_id})
    return response.status_code, response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=False)
