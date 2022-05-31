import os
from dotenv import load_dotenv
import logging
import telegram

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv("API_KEY"))

    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    print(chat_id)
    # Reply with the same message
    bot.sendMessage(chat_id=chat_id, text=update.message.text)
        
    return jsonify({"status": "ok"})