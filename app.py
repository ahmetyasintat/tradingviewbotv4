import telebot 
from flask import Flask, request



app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        price = data['price']
        volume = data['volume']
        alert_tipe = data["alert_tipe"]
        telegramBotApi = data["telegramBotApi"]
        telegramUserId = data["telegramUserId"]

        telebot.TeleBot(telegramBotApi).send_message(telegramUserId, f"ticker = {ticker},price = {price},volume = {volume}")
    except:
        pass
    return {
        "code": "success",
    }