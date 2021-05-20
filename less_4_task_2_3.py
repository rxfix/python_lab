__author__ = 'Нестеренко Александр'

# Задание 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать
# библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать
# результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции
# не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

# Задание 3. Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая
# передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?


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
            value = value.quantize(Decimal('1.00'))  # округлим до двух знаков послез точки
            return value, curr_date


while True:
    in_currency = input('Введите валюту:')
    if currency_rates(in_currency):  # если результат функции найденная валюта и курс
        print(f'{currency_rates(in_currency)[0]}, {currency_rates(in_currency)[1]}')
        # print(type(currency_rates(in_currency)[0])) # <class 'decimal.Decimal'>
        # print(type(currency_rates(in_currency)[1])) # <class 'datetime.date'>
    else:
        print(currency_rates(in_currency))  # если результат функции None
