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
            exchange = str(data["exchange"])
            time = str(data["time"])
            timenow = str(data["timenow"])
            strategy_order= str(data['strategy_order'])
            telegramBotApi = str(data["telegramBotApi"])
            telegramUserId = str(data["telegramUserId"])

            telebot.TeleBot(telegramBotApi).send_message(telegramUserId, f"""  {time}:{timenow}
                                                                               {exchange}:{ticker}, 
                                                                               FİYAT = {price}, 
                                                                               ALARM TİPİ = {strategy_order},
                                                                               """)

        except:
            pass
         
        return {
            "code": "success",
        }
    
if __name__ == "__main__":
    app.run(debug=True)