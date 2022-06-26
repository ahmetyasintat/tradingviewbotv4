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
            strategy_name = str(data["strategy_name"])
            alert_type=str(data["alert_type"])
            strategy_alert_message = str(data["strategy_alert_message"])
            telegramBotApi = str(data["telegramBotApi"])
            telegramUserId = str(data["telegramUserId"])

            telebot.TeleBot(telegramBotApi).send_message(telegramUserId, f"ticker = {ticker}, price = {price},volume = {volume},strategy_name={strategy_name},alert_type = {alert_type},strategy_alert_message = {strategy_alert_message}")

        except:
            pass
         
        return {
            "code": "success",
        }
    
if __name__ == "__main__":
    app.run(debug=True)