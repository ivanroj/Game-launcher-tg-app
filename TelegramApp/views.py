import json, logging
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
from asgiref.sync import async_to_sync

# Импортируйте токен из настроек проекта
from GameLauncher.settings import TELEGRAM_BOT_TOKEN



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
