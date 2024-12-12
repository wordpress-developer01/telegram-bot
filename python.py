import telebot

API_TOKEN = 'YOUR_API_TOKEN_HERE'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который поможет тебе изучить основы языка Python. Напиши 'начать', чтобы начать обучение.")

@bot.message_handler(func=lambda message: message.text.lower() == 'начать')
def start_learning(message):
    bot.reply_to(message, "Отлично! Давай начнем с основ. Что такое переменные? Напиши 'переменные', чтобы узнать больше.")

@bot.message_handler(func=lambda message: message.text.lower() == 'переменные')
def explain_variables(message):
    bot.reply_to(message, "Переменные - это именованные области памяти, которые используются для хранения данных. Например: x = 5.")

@bot.message_handler(func=lambda message: message.text.lower() == 'дальше')
def continue_learning(message):
    bot.reply_to(message, "Хорошо! Теперь давай поговорим о типах данных. Напиши 'типы данных', чтобы узнать больше.")

@bot.message_handler(func=lambda message: message.text.lower() == 'типы данных')
def explain_data_types(message):
    bot.reply_to(message, "В Python есть несколько основных типов данных: int (целые числа), float (числа с плавающей запятой), str (строки) и bool (логические значения).")

bot.polling()
