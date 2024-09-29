import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Твой API токен
API_TOKEN = '7713287680:AAEjz5BhCiIYSQHllKj33l4DmpxqREcbuPU'
bot = telebot.TeleBot(API_TOKEN)

print("Бот запущен...")  # Проверка, что бот стартует

# Функция для получения аватара пользователя через Telegram API
def get_user_avatar(user_id):
    try:
        # Запрос на получение фотографий профиля
        response = requests.get(f"https://api.telegram.org/bot{API_TOKEN}/getUserProfilePhotos?user_id={user_id}&limit=1")
        data = response.json()

        if data['ok'] and data['result']['total_count'] > 0:
            file_id = data['result']['photos'][0][-1]['file_id']  # Самое большое фото

            # Запрос на получение файла
            file_info = requests.get(f"https://api.telegram.org/bot{API_TOKEN}/getFile?file_id={file_id}")
            file_path = file_info.json()['result']['file_path']

            # Генерация полного URL аватара
            avatar_url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file_path}"
            return avatar_url
        else:
            return None
    except Exception as e:
        print(f"Ошибка получения аватара: {e}")
        return None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Получена команда /start")  # Проверка получения команды /start

    # Путь к изображению
    photo_path = 'img/start.png'
    caption_text = "FlipS! Здесь ты можешь флипнуть Hitcoin против другого игрока."

    # Попробуем отправить изображение
    try:
        bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=caption_text)
        print("Изображение отправлено")
    except Exception as e:
        print(f"Ошибка отправки изображения: {e}")

    # Получение аватара пользователя
    avatar_url = get_user_avatar(message.from_user.id)

    # Проверка, был ли получен аватар, и отправка сообщения с аватаром или без него
    if avatar_url:
        bot.send_message(message.chat.id, f"Ваш аватар: {avatar_url}")
    else:
        bot.send_message(message.chat.id, "Не удалось получить аватар")

    # Создание кнопки для Mini App
    markup = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://rouletteoliver.github.io/telegram-mini-app/")
    web_app_button = InlineKeyboardButton("FlipS", web_app=web_app_info)
    markup.add(web_app_button)

    # Попытка отправить сообщение с кнопкой
    try:
        bot.send_message(message.chat.id, "Жми чтобы флипнуть", reply_markup=markup)
        print("Сообщение с кнопкой отправлено")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

bot.polling(none_stop=True, interval=0)  # Параметры для устойчивого подключения
