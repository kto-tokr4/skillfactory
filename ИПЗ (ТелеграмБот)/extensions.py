import requests
from config import keys

class ConversionException(Exception):
    pass

class CalculateCurrency:
    @staticmethod
    def get_price(quote, base, amount):
        if not float(amount):
            raise ConversionException('Указано некорректное значение количества валюты.\n'
                                      'Значение должно представлять собой число и не быть меньше 0.')

        if quote not in keys.keys() or base not in keys.keys():
            raise ConversionException ('Выбранны неккоректные типы валют. Для того чтобы узнать названия доступных валют введите команду "/values".')

        if quote == base:
            raise ConversionException ('Исходная валюта не может совпадать с искомой.')

        response = requests.get(url = 'https://api.currencyapi.com/v3/latest?apikey=cur_live_akUpBLzlQh3X5B74JtowlWdvcuujQyHqi6PR347Y')
        response = response.json()

        quote_value = response['data'][keys[quote]]['value']
        base_value = response['data'][keys[base]]['value']

        total_base = base_value / quote_value
        return round(total_base * float(amount), 2)