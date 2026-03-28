import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

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

print("BOT STARTED")
bot.infinity_polling()
