import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Твой API токен
API_TOKEN = '7713287680:AAFW-S3_71_PbWlNG4K7yIbiR9pkr-t-Y4s'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Загружаем изображение и отправляем его пользователю
    photo_path = 'start.png'  # Укажи путь к изображению
    caption_text = "Нажмите, чтобы играть в Орёл или Решка!"
    
    # Отправляем изображение (замени на актуальный путь к файлу)
    try:
        bot.send_photo(message.chat.id, open(photo_path, 'rb'), caption=caption_text)
    except Exception as e:
        print(f"Ошибка отправки изображения: {e}")

    # Создаем кнопку для запуска Mini App
    markup = InlineKeyboardMarkup()
    web_app_info = WebAppInfo(url="https://rouletteoliver.github.io/telegram-mini-app/")  # Твоя ссылка на Mini App
    web_app_button = InlineKeyboardButton("Играть", web_app=web_app_info)
    markup.add(web_app_button)
    
    # Отправляем сообщение с кнопкой
    bot.send_message(message.chat.id, "Нажмите кнопку ниже для начала игры!", reply_markup=markup)

bot.polling()
