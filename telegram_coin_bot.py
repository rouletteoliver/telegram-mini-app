import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Твой API токен
API_TOKEN = '7713287680:AAFW-S3_71_PbWlNG4K7yIbiR9pkr-t-Y4s'
bot = telebot.TeleBot(API_TOKEN)

print("Бот запущен...")  # Проверка, что бот вообще стартует

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Получена команда /start")  # Проверка получения команды /start
    
    # Путь к изображению
    photo_path = 'start.png'
    caption_text = "Нажмите, чтобы начать лудить!"
    
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

bot.polling(none_stop=True, interval=0)  # Параметры для устойчивого подключения
