__author__ = 'Нестеренко Александр'

from requests import get
from decimal import Decimal
from datetime import datetime


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(
        encoding=response.encoding)  # получаем контент в виде байт кода и декодируем его в строку

    # извлечение даты
    curr_date = response.headers.get('Date').split(' ')  # дуту берем из заголовка сайта
    # date = ['Wed,', '19', 'May', '2021', '16:21:44', 'GMT']
    curr_date = datetime.strptime(f'{curr_date[2]} {curr_date[1]} {curr_date[3]}', '%B %d %Y')
    curr_date = curr_date.date()
    # 2021-05-19

    # поиск курса валюты
    for el in content.split('<CharCode>')[1:]:  # разделяем контент по символу валюты
        char_code = el.split('</CharCode>')
        # ['USD', '<Nominal>1</Nominal><Name>Доллар США</Name><Value>73,6992</Value>...
        if char_code[0] == currency.upper():  # если найден нужный символ валюты не зависимо от регистра
            value = char_code[1].split('<Value>')  # разделяем по курсу валюты
            # ['<Nominal>1</Nominal><Name>Доллар США</Name>', '73,6992</Value><...
            value = value[1].split('</Value>')
            # ['73,6992', '</Valute><Valute ID="R01239"><NumCode>978</NumCode>']
            value = Decimal(value[0].replace(',', '.'))
            # заменяем в найденом элементе списка заппятуюна точку и преобразуем во Decimal
            return value, curr_date


if __name__ == '__main__':  # эта часть не будет выполняться при вызове этого модуля
    print(currency_rates('usd'))
