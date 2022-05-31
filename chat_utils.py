import os
from dotenv import load_dotenv
import requests
from bottle import Bottle, response, request as bottle_request


class telebot_utils:
    def __init__(self):
        load_dotenv()
        API_KEY = os.getenv('API_KEY')
        self.BOT_URL = 'https://api.telegram.org/bot' + API_KEY+ '/'
        self.data = bottle_request.json

        d = bottle_request.json
        self.chat_id = d['message']['chat']['id']

    def get_message(self):
        return self.data['message']['text']

    def send_message(self, msg):
        # HTTP POST- to post chat_id and intended msg
        # sendMessage is a function to send message to telegram bot
        message_url = self.BOT_URL + 'sendMessage'
        requests.post(message_url, json=msg)

    def prepare_data_for_ans(self, answer):
        json_data = {
            "chat_id":self.chat_id,
            "text": answer
        }
        return json_data

    def post_handler(self, answer):
        data = bottle_request.json
        ans_data = self.prepare_data_for_ans(answer)
        self.send_message(ans_data)
        return response
