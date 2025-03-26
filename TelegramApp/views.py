from django.shortcuts import render

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
