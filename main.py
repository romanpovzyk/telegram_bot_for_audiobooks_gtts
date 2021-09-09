from gtts import gTTS
from bot_messages import messages_convert, messages_ready
from config import tg_bot_token
import telebot
import datetime

# bot = telebot.TeleBot(tg_bot_token)
#
# @bot.message_handler(commands=['start'])
# def start_command(message):
#     bot.send_message(message.chat.id, 'Привіт, я — книжковий джин.\nДозволь конвертувати для тебе аудіокнижку.')
#
# @bot.message_handler(commands=['add_text'])
# def _command_(message):
#      bot.send_message(message.chat.id, "Введіть свій текст: ")
#      bot.register_next_step_handler(message, add_user)
#
# bot.polling()


text = input('Введіть сюди ваш текст: \n')
lang = input("Оберіть одну із трьох мов uk/en/ru: ")


# Безпека на випадок неправильного введення
while lang != 'uk' and lang != 'en' and lang != 'ru':
    print('Ми не можемо визначити вашу мову.')

    lang = input("Оберіть одну із семи мов uk/en/ru: ")

    #  Пропуск на випадок правильного введення
    if lang == 'uk' or lang == 'en' or lang == 'ru':
        print('Дякуємо за ваш вибір!')


def convert(text):
    print(messages_convert[lang])
    obj = gTTS(text, lang=lang)
    obj.save('audiobook.mp3')


# Визначаємо час, витрачений на конвертування.
date_start = datetime.datetime.now()
convert(text)
date_end = datetime.datetime.now()
convert_time = date_end - date_start

print(f"{messages_ready[lang]} \n{convert_time}")
