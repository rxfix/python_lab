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


from requests import get, utils
from decimal import Decimal


def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(
        encoding=response.encoding)  # получаем контент в виде байт кода и декодируем его в строку

    date = content.split('<ValCurs Date="')
    date = date[1].split('" name')
    print(date[0])
    for el in content.split('<CharCode>')[1:]:  # разделяем контент по символу валюты
        char_code = el.split('</CharCode>')
        # ['USD', '<Nominal>1</Nominal><Name>Доллар США</Name><Value>73,6992</Value>...
        if char_code[0] == currency.upper():  # если найден нужный символ валюты не зависимо от регистра
            value = char_code[1].split('<Value>')  # разделяем по курсу валюты
            value = value[1].split('</Value>')
            # ['73,6992', '</Valute><Valute ID="R01239"><NumCode>978</NumCode>']
            return Decimal(value[0].replace(',', '.'))
            # заменяем в найденом элементе списка заппятуюна точку и преобразуем во float


print(currency_rates('usd'))
