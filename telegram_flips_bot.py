import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask, jsonify, request
import requests

# Твой API токен
API_TOKEN = '7713287680:AAEjz5BhCiIYSQHllKj33l4DmpxqREcbuPU'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Сохранение аватара пользователя в памяти
user_avatars = {}

@app.route('/api/get_avatar', methods=['GET'])
def get_avatar():
    user_id = request.args.get('user_id')
    avatar_url = user_avatars.get(user_id, None)
    if avatar_url:
        return jsonify({"avatar_url": avatar_url})
    else:
        return jsonify({"error": "Avatar not found"}), 404

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Получена команда /start")  # Проверка получения команды /start

    user_id = message.from_user.id
    photos = bot.get_user_profile_photos(user_id)
    avatar_url = None

    # Если у пользователя есть фото, сохраняем его URL
    if photos.total_count > 0:
        file_id = photos.photos[0][-1].file_id
        file_info = bot.get_file(file_id)
        avatar_url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file_info.file_path}"
        user_avatars[str(user_id)] = avatar_url  # Сохраняем в словаре

    # Отправка стартового изображения
    photo_path = 'img/start.png'
    caption_text = "FlipS! Здесь ты можешь флипнуть Hitcoin против другого игрока."

    try:
        bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=caption_text)
    except Exception as e:
        print(f"Ошибка отправки изображения: {e}")

    # Создание кнопки для Mini App
    markup = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://rouletteoliver.github.io/telegram-mini-app/")
    web_app_button = InlineKeyboardButton("FlipS", web_app=web_app_info)
    markup.add(web_app_button)

    bot.send_message(message.chat.id, "Жми чтобы флипнуть", reply_markup=markup)

if __name__ == "__main__":
    # Запуск Flask API и бота
    bot.polling(none_stop=True, interval=0)
    app.run(host="0.0.0.0", port=5000)  # Запуск API для получения аватаров
