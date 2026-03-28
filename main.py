import os
import telebot
from flask import Flask
from flask import send_file
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/ping")
def ping():
    return {"status": "ok"}
@app.route("/app")
def web_app():
    return send_file("index.html")
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

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
    bot.infinity_polling()

if __name__ == "__main__":
    import threading
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
