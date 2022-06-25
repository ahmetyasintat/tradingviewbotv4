from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from flask import Flask, request
import telebot
import json

app = Flask(__name__)

token = "5449738034:AAFSs_WqNNfPCUqFT_oo_v0JlCz8wAbh-iA"
@app.route("/webhook", methods=['POST'])
def webhook():
    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        price = data['price']
        volume = data['volume']
        alert_tipe = data["alert_tipe"]
        telegramUserId = data["telegramUserId"]

        a = telebot.TeleBot(token).send_message(telegramUserId, f"ticker = {ticker},price = {price},volume = {volume}")

        def start(update, context):
            update.message.reply_text(a)

        updater = Updater(token)
        updater.dispatcher.add_handler(CommandHandler("start",start))
        updater.start_polling()
    except:
        pass
    return {
        "code": "success",
    }


