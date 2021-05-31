import re

# # RE_NAME = re.compile(r'^[А-ЯЁ][а-яё]+$')
#
# RE_DATE = re.compile(r'^(\d{2}.){2}\d{4}$')
#
#
# def name_is_valid(name):
#     return RE_DATE.match(name)
#
#
# if __name__ == '__main__':
#     while True:
#         name = input('Введите имя:\n')
#         if name_is_valid(name):
#             break
#     print(f'пользователь: {name}')


#################
#
# import re
#
# RE_DATE = re.compile(r'^(\d{2}[.~,/-]){2}\d{4}$')
# for date in ['23.01.2021', '23-01-2021', '23~01~2021']:
#    assert RE_DATE.match(date), f'wrong date {date}'
#    print(RE_DATE.match(date))


#################
# import re
#
#
# RE_DATE = re.compile(r'(?:\d{2}[./-]){2}\d{4}')
#
# txt = 'Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - очень холодно. ' \
#      'Надеемся, что 24-01-2021 будет без ветра.'
#
# print(RE_DATE.findall(txt))
# print(dir(RE_DATE))


#################

# import re
#
# RE_PRODUCTS = re.compile(r'"([^"]+)"\s*\((\d+(?:[,.]\d+)*).*\)')
#
# txt = '''
# Иван сегодня сделал заказ: "iPhone 12"  (158900,6 руб),
# "Galaxy S21"(98653.7 р).
# Позже он добавил в корзину "iPad"\t(32451)
# '''
#
# print(RE_PRODUCTS.findall(txt))


#################


# import re
#
# RE_EQ_LETTERS = re.compile(r'\b(\w)\w*\1\b', re.IGNORECASE)
# txt = 'Однако, хорошо у вас получилось. А как еще могло быть?'
#
# print(RE_EQ_LETTERS.findall(txt))
# print(RE_EQ_LETTERS.search(txt))
# print(RE_EQ_LETTERS.match(txt))
# print(*RE_EQ_LETTERS.finditer(txt))


#################

# import re
#
# RE_GET_PARSER = re.compile(r'(?<=[&?])(?P<key>[^&]+)=(?P<val>[^&]+)(?=&*)')
#
# url = 'https://translate.google.com/?hl=ru&sl=en&tl=ru&text=go&op=translate'
#
# print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(url)), sep=', ')



#################


# import re
#
# # result = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, ''test.first@analyticsvidhya.com, first.test@rest.biz')
# result = re.findall(r'((?:\d+\.){3}\d)(?:(?:\s\-){2}\s\[)(\d+\/\w+\/(?:\d+:){3}\d+.+\d+)(?:\]\s")(\w+)(?:\s)((?:\/\w+){0,10})(?:\s\w+\/\d+\.\d+"\s)(\d+)(?:\s)(\d+)', '93.180.71.3 - - [17/May/2015:08:05:26 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')
# # result = re.findall(r'((?:\d+\.){3}\d)\s\-\s\-|\[(\d+\/\w+\/(?:\d+:){3}\d+.\+\d+)|(?:\]\s)\"(\w+)|((?:\/\w+){2})|(HTTP\/1.1"\s)(\d+)', '93.180.71.3 - - [17/May/2015:08:05:26 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')
# # result = re.findall(r'(?:\].)\"(\w+)', '93.180.71.3 - - [17/May/2015:08:05:26 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')
# # result = re.search(r'((?:\d+\.){3}\d)\s\-\s\-|((?:\/\w+){2}).HTTP', '93.180.71.3 - - [17/May/2015:08:05:26 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')
# # result = re.findall(r'((?:\d+\.){3}\d)\s\-\s\-|((?:\/\w+){2}).HTTP', '93.180.71.3 - - [17/May/2015:08:05:26 +0000] "GET /downloads/product_1 HTTP/1.1" 404 324 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"')
# result = re.findall(r'((?:\d+\.){3}\d)(?:(?:\s\-){2}\s\[)(\d+\/\w+\/(?:\d+:){3}\d+.+\d+)(?:\]\s")(\w+)(?:\s)((?:\/\w+){0,10})(?:\s\w+\/\d+\.\d+"\s)(\d+)(?:\s)(\d+)', 'b5.63.153.40 - - [01/Jun/2015:16:06:28 +0000] "GET /downloads/product_1 HTTP/1.1" 200 490 "-" "Debian APT-HTTP/1.3 (0.9.7.8)"')
#
#
#
# print(result)
# # print(result.group(2))


############


# def p_wrapper(func):
#    print(func, '55555')
#
#    def tag_wrapper(*args, **kwargs):
#        print('args', args)
#        print('kwargs', kwargs)
#        markup = func(*args, **kwargs)
#        print(markup)
#        return markup
#
#    return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#    return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# print(render_input)



##############


# def p_wrapper(func):
#    def tag_wrapper(*args, **kwargs):
#        print('args', args)
#        print('kwargs', kwargs)
#        markup = func(*args, **kwargs)
#        return f'<p>{markup}</p>'
#
#    return tag_wrapper
#
#
# @p_wrapper
# def render_input(field,**kwargs):
#    return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username', d=9)
# print(username_f)




###########


#
# def simple_cache(func):
#    cache = {}
#
#    def wrapper(*args):
#        # nonlocal cache
#        key = str(*args)
#        if key not in cache:
#            cache[key] = func(*args)
#        return cache[key]
#
#    return wrapper
#
#
# @simple_cache
# def render_input(field):
#    print(f"call render_input('{field}')")
#    return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)




##########

#
#
# from time import perf_counter
#
# print(f'{perf_counter()}: script started')
#
#
# def simple_cache(func):
#    cache = {}
#    print(f'{perf_counter()}: {func.__name__} cache created ({id(cache)})')
#
#    def wrapper(*args):
#        nonlocal cache
#        key = tuple(args)
#        if key not in cache:
#            cache[key] = func(*args)
#        return cache[key]
#
#    return wrapper
#
#
# @simple_cache
# def calc_sum(x, y):
#    return x + y
#
#
# @simple_cache
# def calc_mul(x, y):
#    return x * y
#
# print(calc_sum(5, 6))



###########
# def simple_cache(func):
#    cache = {}
#
#    def wrapper(*args):
#        nonlocal cache
#        key = str(*args)
#        if key not in cache:
#            cache[key] = func(*args)
#        return cache[key]
#
#    return wrapper
#
#
# def logger(func):
#    def wrapper(*args):
#        result = func(*args)
#        print(f'\tcall {func.__name__}({", ".join(map(str, args))})')
#        return result
#
#    return wrapper
#
#
# @simple_cache
# @logger
# def render_input(field):
#    return f'<input id="id_{field}" type="text" name="{field}">'
# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)



##############


# from functools import wraps
#
#
# def simple_cache(func):
#    cache = {}
#
#    @wraps(func)
#    def wrapper(*args):
#        nonlocal cache
#        key = str(*args)
#        if key not in cache:
#            cache[key] = func(*args)
#        return cache[key]
#
#    return wrapper
#
#
# def logger(func):
#    def wrapper(*args):
#        result = func(*args)
#        print(f'\tcall {func.__name__}({", ".join(map(str, args))})')
#        return result
#
#    return wrapper
#
#
# @logger
# @simple_cache
# def render_input(field):
#    return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# password_f = render_input('password')
# username_f_2 = render_input('username')
# print(username_f)
# print(password_f)
# print(username_f_2)



################

def logger(verbosity=0):
   def _logger(func):
       def wrapper(*args):
           result = func(*args)
           msg = f'\tcall {func.__name__}'
           if verbosity > 0:
               msg = f'{msg}({", ".join(map(str, args))})'
           if verbosity > 1:
               msg = f'{msg} -> {result}'
           return msg

       return wrapper

   return _logger


@logger(verbosity=2)
def render_input(field):
   return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
password_f = render_input('password')
print(username_f)
print(password_f)