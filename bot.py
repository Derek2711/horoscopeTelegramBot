import os
import telebot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello", "hi"])
def send_welcome(message):
    bot.reply_to(message, "Hello! MaDaFaKa")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()
