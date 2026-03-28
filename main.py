import telebot
import os
from flask import Flask, render_template

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__, template_folder="templates")

# --- САЙТ ---
@app.route("/")
def index():
    return "SITE WORKING"

# --- БОТ (ПОКА НЕ ЗАПУСКАЕМ) ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает")

# --- ЗАПУСК ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print("STARTING WEB SERVER ON PORT", port)

    app.run(host="0.0.0.0", port=port)
