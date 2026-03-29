import os
import threading
import telebot
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- САЙТ ---
@app.route("/")
def index():
    return "SITE WORKING"

# --- БОТ ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    web_app = WebAppInfo("https://telegram-bot-production-af15.up.railway.app")

    button = InlineKeyboardButton(
        text="🎰 Играть",
        web_app=web_app
    )

    markup.add(button)

    bot.send_message(
        message.chat.id,
        "Жми кнопку 👇",
        reply_markup=markup
    )

def run_bot():
    bot.infinity_polling()

# --- ЗАПУСК ---
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
