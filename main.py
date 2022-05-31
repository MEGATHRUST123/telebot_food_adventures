# main python file for telebot
import os
from re import A
from dotenv import load_dotenv
from bottle import run, post, response, request as bottle_request
import pandas as pd
import numpy as np
from chat_utils import telebot_utils
# import response file
import response as R

# Get API key from environment variables file aka variable text file
# listens to update from telegram bot
# https://api.telegram.org/bot5476596922:AAHgZcwx8sgKQGDsqAGuCpgfbJbO5yiM2gg/setWebHook?url=https://https://1bcc-116-15-129-80.ap.ngrok.io/
# Webhook: {"ok":true,"result":true,"description":"Webhook was set"}
@post('/') # our python function based endpoint
def main():
    # import telebot utils
    print("=== import telegram bot utilies ===")
    telebot = telebot_utils()
    msg = telebot.get_message()
    reply = R.sample_response(input_text=msg)
    telebot.post_handler(answer=reply)

if __name__=='__main__':
    run(host='localhost', port=8080, debug=True)


