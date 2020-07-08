"""

this script runs a bot on telegram

for this script to run please install the next modules:
    sudp pip3 install dateparser pandas-datareader python-telegram-bot telegram python-binance

"""

from telegram.ext import Updater
from datetime import datetime
import pandas_datareader as web
import dateparser
from binance.client import Client
#import keys

token = open("keys.py","r").readline().strip()
# koken = keys
updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")                     

def get_FB(update, context):

    start = dateparser.parse("yesterday")
    end = dateparser.parse("today")

    FB = web.DataReader('fb', 'yahoo', start, end)

    results = "High = " + FB.High.to_string().split()[2] + " - " \
       "Low = " + FB.Low.to_string().split()[2] + " - \n " \
       "Open = " + FB.Open.to_string().split()[2] + " - \n " \
       "Close = " + FB.Close.to_string().split()[2] + " - " \
       "Volume = " + FB.Volume.to_string().split()[2]

    context.bot.send_message(chat_id=update.effective_chat.id, text=results)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

FB_hendler = CommandHandler("FB", get_FB)
dispatcher.add_handler(FB_hendler)


updater.start_polling()
