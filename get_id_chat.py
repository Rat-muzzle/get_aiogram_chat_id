from aiogram.filters.command import Command
from aiogram.types import Message, BotCommandScopeDefault
from aiogram import Bot, Dispatcher, html
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os, asyncio, logging


logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")


dp = Dispatcher()

@dp.message()
async def send_chat_id(message: Message):
    """Обработчик команды /chat_id"""
    logging.info(f"Новое сообщение в группе {message.chat.id} от {message.from_user.id}")
    chat = message.chat

    response = (
        f"🆔 <b>Chat ID</b>: <code>{chat.id}</code>\n"
        f"👥 <b>Тип чата</b>: {chat.type}\n"
    )

    # Добавляем дополнительную информацию в зависимости от типа чата
    if chat.title:
        response += f"📛 <b>Название</b>: {chat.title}\n"
    if chat.username:
        response += f"👤 <b>Юзернейм</b>: @{chat.username}\n"

    # Добавляем пояснение
    response += "\nℹ️ <i>Используйте этот ID для взаимодействия с API Telegram</i>"

    await message.reply(response)


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # sql_total.sql_registr(124124, 'login', 'password', 'note')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await bot.set_my_commands(scope=BotCommandScopeDefault())


if __name__ == '__main__':

    asyncio.run(main())