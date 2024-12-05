import telebot
from config import token, keys
from extensions import *


bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['help','start'])
def get_info(message):
    text = ('Для получения курса валют введите сообщение по форме: \n'
            '<Исходная валюта> <Искомая валюта> <Количество> \n'
            'Для получения доступных валюты введите "/values"')
    bot.reply_to(message, text=text)

@bot.message_handler(commands=['values'])
def get_currency_info(message):
    text = 'Список доступных валют:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text=text)

@bot.message_handler(content_types=['text'])
def get_calculation(message):
    try:
        quote, base, amount = message.text.split(' ')
        try:
            total_base = CalculateCurrency.get_price(quote, base, amount)
            bot.reply_to(message, text=f'Цена {amount} {quote} в {base} - {total_base}.')
        except ConversionException as e:
            bot.reply_to(message, text=f'{e}')
    except Exception :
        bot.reply_to(message, text='Указан некорректный запрос. \n'
                                   'Сообщение должно соответствовать форме указанной в "/help"')

bot.polling(none_stop=True)