from gtts import gTTS
from bot_messages import messages_convert, messages_ready, start_messages
from config import tg_bot_token
import telebot
import datetime

bot = telebot.TeleBot(tg_bot_token)

lang = ''


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, start_messages['pos'])
    else:
        bot.send_message(message.from_user.id, start_messages['neg'])
    bot.register_next_step_handler(message, get_lang)


def get_lang(message):
    if message.text == "/uk":
        bot.send_message(message.from_user.id, "Дякую за вибір української мови. Надішли текст.")
    elif message.text == "/en":
        bot.send_message(message.from_user.id, "Дякую за вибір англійської мови. Надішли текст.")
    elif message.text == "/ru":
        bot.send_message(message.from_user.id, "Дякую за вибір російської мови. Надішли текст.")
    else:
        bot.send_message(message.from_user.id, "Не розумію тебе, введи /uk або /en або /ru")
    global lang
    lang = message.text[1:]
    bot.register_next_step_handler(message, get_audio)


def convert(message):
    obj = gTTS(message, lang=lang)
    obj.save('audiobook_for_you.mp3')


def get_audio(message):
    if len(message.text) > 6:
        bot.send_message(message.from_user.id, 'Дякую, текст отримав.')
        date_start = datetime.datetime.now()
        convert(message.text)
        date_end = datetime.datetime.now()
        convert_time = date_end - date_start
        bot.send_message(message.from_user.id, f"Твій текст готовий. На це пішло {convert_time}")
    audio = open('audiobook_for_you.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()


bot.polling(none_stop=True, interval=0)
