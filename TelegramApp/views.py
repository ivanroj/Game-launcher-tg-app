import json, logging
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
from asgiref.sync import async_to_sync

# Импортируйте токен из настроек проекта
from GameLauncher.settings import TELEGRAM_BOT_TOKEN

# Создаем приложение с помощью ApplicationBuilder (python-telegram-bot v20+)
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

logger = logging.getLogger(__name__)

# Асинхронный обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # URL мини-приложения
    web_app_url = "https://telegram-app-richardyoung.amvera.io/"

    # Создаем кнопку с объектом InlineKeyboardButton, передавая параметр web_app
    keyboard = [
        [
            InlineKeyboardButton(
                text="Игровой лаунчер",
                web_app={"url": web_app_url}
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Добро пожаловать! Запустите мини-приложение:",
        reply_markup=reply_markup
    )


# Регистрируем обработчик команды /start
application.add_handler(CommandHandler("start", start))


# Синхронный view для обработки webhook-обновлений от Telegram
@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            logger.info(f"Получено обновление: {data}")  # Логируем входящие данные
            update = Update.de_json(data, application.bot)
        except Exception as e:
            logger.error(f"Ошибка декодирования: {e}")
            return HttpResponseBadRequest(f"Ошибка декодирования: {e}")

        async_to_sync(application.process_update)(update)
        return JsonResponse({"status": "ok"})
    return HttpResponseBadRequest("Метод не поддерживается")

def miniapp_home(request):
    # Список игр, которые будут отображаться на главном экране
    games = [
        {"name": "Шашки", "url": "/games/checkers/"},
        {"name": "Шахматы", "url": "/games/chess/"},
        {"name": "Тетрис", "url": "/games/tetris/"},
        {"name": "Сапёр", "url": "/games/minesweeper/"},
        {"name": "Косынка", "url": "/games/solitaire/"},
    ]
    return render(request, "TelegramApp/miniapp_home.html", {"games": games})

# def tetris_game(request):
#     return render(request, "TelegramApp/tetris.html")
