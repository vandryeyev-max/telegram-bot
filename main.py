import os
import telebot
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/ping")
def ping():
    return {"status": "ok"}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает 🚀")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
