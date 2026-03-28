import telebot
import os
import threading
from flask import Flask, send_from_directory
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- САЙТ ---
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# --- БОТ ---
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()

    web_app = WebAppInfo("https://production-b86b.up.railway.app")

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

# --- ЗАПУСК БОТА ---
def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot).start()

print("BOT + SITE STARTED")

# ❗ ВАЖНО — ПОРТ
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
