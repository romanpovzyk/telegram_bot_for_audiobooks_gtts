from gtts import gTTS
from bot_messages import messages
from config import tg_bot_token
import telebot
import datetime

bot = telebot.TeleBot(tg_bot_token)

lang = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('start', '/uk', '/en', '/ru', '/help')
    bot.send_message(message.chat.id, messages['general']['start'], reply_markup=keyboard)


@bot.message_handler(commands=['uk', 'en', 'ru'])
def get_lang(message):
    global lang
    lang = message.text[1:3]
    bot.send_message(message.from_user.id, messages[lang]['thanks'])
    bot.register_next_step_handler(message, get_audio)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.from_user.id, messages['general']['help'])


def get_audio(message):
    if len(message.text) > 6:
        bot.send_message(message.from_user.id, messages[lang]['received_text'])

        date_start = datetime.datetime.now()

        obj = gTTS(message.text, lang=lang)
        date_name = str(date_start).replace(':', '_')
        file_name = f'audiobook_for_you_{date_name}.mp3'
        obj.save(file_name)

        date_end = datetime.datetime.now()

        bot.send_message(message.from_user.id, f"{messages[lang]['text_with_time']} {date_end - date_start}")

        audio = open(file_name, 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()

    else:
        bot.send_message(message.from_user.id, messages[lang]['short_text'])


bot.polling(none_stop=True, interval=0)
