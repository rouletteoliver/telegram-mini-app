import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask, send_from_directory

# Твой API токен
API_TOKEN = '7713287680:AAEjz5BhCiIYSQHllKj33l4DmpxqREcbuPU'
bot = telebot.TeleBot(API_TOKEN)

# Инициализация Flask
app = Flask(__name__)

# Маршрут для обслуживания основного файла index.html
@app.route('/')
def serve():
    return send_from_directory('public', 'index.html')

# Маршрут для обслуживания статических файлов
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('public', path)

print("Бот запущен...")  # Проверка, что бот вообще стартует

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Получена команда /start")  # Проверка получения команды /start
    
    # Путь к изображению
    photo_path = 'img/start.png'
    caption_text = "Приветствую тебя во FlipS! Здесь ты можешь флипнуть Hitcoin против другого игрока."
    
    # Попробуем отправить изображение
    try:
        bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=caption_text)
        print("Изображение отправлено")
    except Exception as e:
        print(f"Ошибка отправки изображения: {e}")

    # Создание кнопки для Mini App
    markup = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://rouletteoliver.github.io/telegram-mini-app/")
    web_app_button = InlineKeyboardButton("Лудить", web_app=web_app_info)
    markup.add(web_app_button)
    
    # Попытка отправить сообщение с кнопкой
    try:
        bot.send_message(message.chat.id, "Нажмите кнопку ниже для начала игры!", reply_markup=markup)
        print("Сообщение с кнопкой отправлено")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

# Запуск Flask и бота
if __name__ == "__main__":
    # Запуск Flask сервера
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))).start()

    # Запуск бота
    bot.polling(none_stop=True, interval=0)  # Параметры для устойчивого подключения
