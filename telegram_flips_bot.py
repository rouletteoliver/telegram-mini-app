import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Твой API токен
API_TOKEN = '7713287680:AAEjz5BhCiIYSQHllKj33l4DmpxqREcbuPU'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id  # Получаем ID пользователя

    # Путь к изображению и текст приветствия
    photo_path = 'img/start.png'
    caption_text = "FlipS! Здесь ты можешь флипнуть Hitcoin против другого игрока."

    # Отправка изображения
    try:
        bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=caption_text)
    except Exception as e:
        print(f"Ошибка отправки изображения: {e}")

    # Получение аватара пользователя через API Telegram
    avatar_url = get_user_avatar(API_TOKEN, user_id)
    
    # Отправка данных в чат с кнопкой для открытия Mini App
    markup = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://rouletteoliver.github.io/telegram-mini-app/")
    web_app_button = InlineKeyboardButton("FlipS", web_app=web_app_info)
    markup.add(web_app_button)
    
    try:
        bot.send_message(
            message.chat.id, 
            f"Ваш аватар: {avatar_url}\nЖми чтобы флипнуть", 
            reply_markup=markup
        )
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

# Функция для получения URL аватара пользователя
def get_user_avatar(bot_token, user_id):
    url = f"https://api.telegram.org/bot{bot_token}/getUserProfilePhotos?user_id={user_id}"
    response = requests.get(url)
    data = response.json()

    if 'result' in data and data['result']['total_count'] > 0:
        file_id = data['result']['photos'][0][0]['file_id']
        file_info_url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
        file_info_response = requests.get(file_info_url).json()
        file_path = file_info_response['result']['file_path']
        avatar_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
        return avatar_url
    return None

bot.polling(none_stop=True, interval=0)
