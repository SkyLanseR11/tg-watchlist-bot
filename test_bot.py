import os
from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
