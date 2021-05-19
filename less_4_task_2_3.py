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
    curr_date = content.split('<ValCurs Date="')
    # ['<?xml version="1.0" encoding="windows-1251"?>', '19.05.2021" name="Foreign Currency Mar
    curr_date = curr_date[1].split('" name')
    # ['19.05.2021', '="Foreign Currency Market"
    curr_date = curr_date[0].split('.')
    # ['19', '05', '2021']
    curr_date = datetime(year=int(curr_date[2]), month=int(curr_date[1]), day=int(curr_date[0]))
    # 2021-05-19 00:00:00
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


if __name__ == '__main__':  # эта часть не будет выполняться при вызове этог модуля
    print(currency_rates('usd'))
