#!/usr/bin/env python3
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RASA_URL = os.getenv("RASA_URL", "http://localhost:5005/webhooks/rest/webhook")
BOT_TOKEN = "8205206073:AAHV-d3ikOEm6Wy6K7zHXGw3ysbtU6skuog"

@app.route('/webhooks/telegram/webhook', methods=['POST'])
def telegram_webhook():
    print(f"Received webhook: {request.json}")
    data = request.json
    
    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')
        print(f"Processing message: {text} from chat: {chat_id}")
        
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
                    print(f"Sending to Telegram: {response['text']}")
                    result = send_telegram_message(chat_id, response['text'])
                    print(f"Telegram send result: {result}")
    
    return jsonify({"status": "ok"})

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": chat_id, "text": text})
    return response.status_code, response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=False)
