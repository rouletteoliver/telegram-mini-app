worker: python telegram_flips_bot.py
web: gunicorn -w 4 -b 0.0.0.0:$PORT telegram_flips_bot:bot
web: python3 -m http.server $PORT
