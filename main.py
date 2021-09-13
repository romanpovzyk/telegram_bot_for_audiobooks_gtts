from gtts import gTTS
from bot_messages import messages
# from config import tg_bot_token
import telebot
import datetime

bot = telebot.TeleBot('1952440948:AAEv2sXDF-nb0rR-CtCpTPJRJczGmLOqcGE')

lang = ''


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, messages['start_messages']['greeting'])
    else:
        bot.send_message(message.from_user.id, messages['start_messages']['unknown'])
    bot.register_next_step_handler(message, get_lang)


def get_lang(message):
    if message.text == "/uk":
        bot.send_message(message.from_user.id, messages['thanks_messages']['uk'])
    elif message.text == "/en":
        bot.send_message(message.from_user.id, messages['thanks_messages']['en'])
    elif message.text == "/ru":
        bot.send_message(message.from_user.id, messages['thanks_messages']['ru'])
    else:
        bot.send_message(message.from_user.id, messages['thanks_messages']['unknown'])
    global lang
    lang = message.text[1:]
    bot.register_next_step_handler(message, get_audio)


def get_audio(message):
    if len(message.text) > 6:
        bot.send_message(message.from_user.id, messages['received_text'])
        date_start = datetime.datetime.now()

        obj = gTTS(message.text, lang=lang)
        date_name = str(date_start).replace(':', '_')
        file_name = f'audiobook_for_you_{date_name}.mp3'
        obj.save(file_name)

        date_end = datetime.datetime.now()
        convert_time = date_end - date_start
        bot.send_message(message.from_user.id, f"{messages['text_with_time']} {convert_time}")
        audio = open(file_name, 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
    elif len(message.text) <= 6:
        bot.send_message(message.from_user.id, messages['short_text'])


bot.polling(none_stop=True, interval=0)
