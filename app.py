from distutils.log import debug
import telebot 
from flask import Flask, request




app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
        try:
            data = request.json
            ticker = str(data['ticker'])
            price = str(data['price'])
            volume = str(data['volume'])
            buy = str(data[buy])
            telegramBotApi = str(data["telegramBotApi"])
            telegramUserId = str(data["telegramUserId"])

            telebot.TeleBot(telegramBotApi).send_message(telegramUserId, f"ticker = {ticker}, price = {price},volume = {volume},BUY_Alert = {buy}")

        except:
            pass
         
        return {
            "code": "success",
        }
    
if __name__ == "__main__":
    app.run(debug=True)