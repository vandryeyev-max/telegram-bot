import os
import telebot
from flask import Flask, send_file
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/app")
def web_app():
    return send_file("index.html")

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    btn = InlineKeyboardButton(
        text="🎮 Открыть казино",
        web_app={"url": "https://telegram-bot-production-b86b.up.railway.app/app"}
    )

    markup.add(btn)

    bot.send_message(message.chat.id, "Жми кнопку 👇", reply_markup=markup)

def run_bot():
    while True:
        try:
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print("Ошибка:", e)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
