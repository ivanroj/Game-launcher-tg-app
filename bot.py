import logging
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiohttp import web
from GameLauncher.settings import TELEGRAM_BOT_TOKEN

# Укажите ваш токен Telegram-бота
TOKEN = TELEGRAM_BOT_TOKEN

# Публичный URL вашего сервера (домен, выданный Amvera)
WEBHOOK_HOST = "https://telegram-app-richardyoung.amvera.io"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Ссылка на ваше Mini App приложение
MINI_APP_URL = "https://telegram-app-richardyoung.amvera.io/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✨ Play Tonique ✨", web_app=WebAppInfo(url=MINI_APP_URL))]
        ]
    )
    await message.answer("Привет! Для входа в приложение нажми на кнопку ниже:", reply_markup=keyboard)

async def on_startup(app: web.Application):
    # Устанавливаем webhook
    await bot.set_webhook(WEBHOOK_URL)
    logging.info(f"Webhook установлен: {WEBHOOK_URL}")

async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    logging.info("Webhook удалён")

async def handle_webhook(request: web.Request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return web.Response()

def main():
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, handle_webhook)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, host="0.0.0.0", port=80)

if __name__ == "__main__":
    main()



















# import logging
# from aiogram import Bot, Dispatcher, Router
# from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
# from aiogram.filters import Command
# import asyncio
#
# # Укажите ваш токен Telegram-бота
# TOKEN = "7902554187:AAGOonAt1igThUgAVto22LdyHfEcp5wH0FQ"
# # Укажите ссылку на ваше Mini App приложение
# MINI_APP_URL = "https://telegram-app-richardyoung.amvera.io/"
#
# # Включаем логирование
# logging.basicConfig(level=logging.INFO)
#
# # Создаём объекты бота и диспетчера
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
# router = Router()
#
# dp.include_router(router)
#
# @router.message(Command("start"))
# async def send_welcome(message: Message):
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[[InlineKeyboardButton(text="✨ Play Tonique ✨", web_app=WebAppInfo(url=MINI_APP_URL))]]
#     )
#     await message.answer("Привет! Для входа в приложение нажми на кнопку ниже:", reply_markup=keyboard)
#
# async def main():
#     # await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
#
