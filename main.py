import telebot
import os
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask, render_template

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# ВАЖНО — явно указываем папку templates
app = Flask(__name__, template_folder="templates")

# --- САЙТ ---
@app.route("/")
def index():
    return "SITE WORKING"

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

# --- СТАРТ ---
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
