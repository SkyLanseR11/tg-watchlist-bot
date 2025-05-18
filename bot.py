import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        f"Привет! Я чат-бот помогающий тебе одному или с кем-то\
        вместе вести список просмотренного. Набери команду /help, чтобы узнать все команды"
    )


@dp.message(Command(commands=["help"]))
async def process_start_command(message: Message):
    await message.answer(
        f"У меня есть следующие команды:\n"
        f"/start - Запуск бота\n"
        f"/help - Список команд бота\n"
        f"/contacts - Контакты для связи\n"
        f"/add - Добавить фильм, сериал и т.д. (ссылка на него из kinopoisk.ru, kinorium.ru)\n"
        f"/list - Список добавленных фильмов\n"
        f"/del - Удалить фильм (по введенной ссылке)"
    )


@dp.message(Command(commands=["echo"]))
async def process_start_command(message: Message):
    await message.answer(
        "Напиши мне что-нибудь и в ответ" "я пришлю тебе твое сообщение"
    )


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=f"А я повторю за тобой:\n{message.text}")


if __name__ == "__main__":
    dp.run_polling(bot)
