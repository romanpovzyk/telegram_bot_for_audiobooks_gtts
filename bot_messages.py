messages = {
    'general': {
        'start': """
Привіт, хочу конвертувати тобі книгу.
Якою мовою у тебе текст?
    /uk — українською
    /en — англійською
    /ru — російською
""",
        'help': """
Введи /start для переходу на початок. 
Або ж обери, будь ласка, мову для начитки: 
    /uk — українську
    /en — англійську
    /ru — російську
"""
    },
    'uk': {
        'thanks': """
Дякую за вибір української мови.
Надішли, будь ласка, свій текст.
""",
        'received_text': "Дякую, текст отримав.",
        'text_with_time': """
Твій текст готовий. 
На це пішло""",
        'short_text': """
Текст замалий для начитки.
Ця сесія закінчилася. Натисни /start для нової спроби.
""",
        'command_mistake': """
Це команда, а не текст.
Ця сесія закінчилася. Натисни /start для нової спроби.
"""
    },
    'en': {
        'thanks': """
Thank you for choosing English. 
Please send your text.
""",
        'received_text': "Thank you, I received the text.",
        'text_with_time': """
Your text is ready. 
It took""",
        'short_text': """
The text is too small to read.
This session is over. Press /start for a new attempt.
""",
        'command_mistake': """
This is a command, not a text.
This session is over. Press /start for a new attempt.
"""
    },
    'ru': {
        'thanks': """
Спасибо за выбор русского языка. 
Пришли, пожалуйста, свой текст.
""",
        'received_text': "Спасибо, текст получил.",
        'text_with_time': """
Твой текст готов. 
На это ушло""",
        'short_text': """
Текст слишком короткий для начитки.
Эта сессия закончилась. Нажми / start для новой попытки.
""",
        'command_mistake': """
Это команда, а не текст.
Эта сессия закончилась. Нажми /start для новой попытки.
"""
    }
}
