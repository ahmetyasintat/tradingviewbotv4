from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from flask import Flask, request
import telebot
import json

app = Flask(__name__)

token = "5449738034:AAFSs_WqNNfPCUqFT_oo_v0JlCz8wAbh-iA"
@app.route("/webhook", methods=['POST'])
def webhook(update, context):
    a = telebot.TeleBot(token).send_message("-1001400179510", f"ticker = {ticker},price = {price},volume = {volume}")
    update.message.reply_text(a)

updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler("start",webhook))
updater.start_polling()
