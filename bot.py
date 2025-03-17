import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
import asyncio

# Укажите ваш токен Telegram-бота
TOKEN = "7902554187:AAGOonAt1igThUgAVto22LdyHfEcp5wH0FQ"
# Укажите ссылку на ваше Mini App приложение
MINI_APP_URL = "https://telegram-app-richardyoung.amvera.io/"

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

dp.include_router(router)

@router.message(Command("start"))
async def send_welcome(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="✨ Play Tonique ✨", web_app=WebAppInfo(url=MINI_APP_URL))]]
    )
    await message.answer("Привет! Для входа в приложение нажми на кнопку ниже:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


