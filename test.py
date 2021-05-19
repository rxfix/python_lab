import sys

#
#
#
#
# from time import perf_counter
#
# start = perf_counter()
# nums = []
# for num in range(1, 10 ** 6 + 1, 2):
#    nums.append(num ** 2)
# print(type(nums), sys.getsizeof(nums))
#
# nums_sum = sum(nums)
# print(nums_sum, perf_counter() - start)
# # 166666666666500000 0.022040908999999997
#
# start = perf_counter()
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(type(nums_gen), sys.getsizeof(nums_gen))
# # nums_gen_sum = sum(nums_gen)
# # print(nums_gen_sum, perf_counter() - start)
#
#
# nums = []
# for num in range(1, 10 ** 6 + 1, 2):
#    nums.append(num ** 2)
#
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
#
# print(nums[:3])
# # [1, 9, 25]
# print(next(nums_gen), next(nums_gen), next(nums_gen), sep=', ')
# from itertools import islice
# print(*islice(nums_gen, 3))  # 49 81 121
#
# nums_gen = (num**2 for num in range(1, 100))
# print(type(nums_gen), sys.getsizeof(nums_gen))
# # nums_gen_sum = sum(nums_gen)
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
#
# # eng_letters_gen = (chr(code) for code in range(ord('#'), ord('~') + 1))
# # print(*eng_letters_gen, sep='')
#
#
# import sys
#
#
# def nums_generator(max_num):
#    for num in range(1, max_num + 1, 2):
#        yield num ** 2
#
#
# nums_gen = nums_generator(10 ** 6)
# print(type(nums_gen), sys.getsizeof(nums_gen))  # <class 'generator'> 112
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
#
# def letters_generator(start, end):
#    for code in range(ord(start), ord(end) + 1):
#        yield chr(code)
# #
# #
# # eng_uppercase_letters = letters_generator('A', 'Z')
# # print(*eng_uppercase_letters, sep='')
#
# nums_cube_gen = (num ** 3 for num in range(5 + 1))
# nums_cube = list(nums_cube_gen)
# print(type(nums_cube), *nums_cube)
#
# nums_cube = [num ** 3 for num in range(5 + 1)]
# print(type(nums_cube), *nums_cube)
#
# weather_data = [
#    [-17.5, -18.9, -21.0, -16.1],
#    [-9.3, -11.7, -14.3, -15.8],
# ]
#
# flat_weather_data = []
# for row in weather_data:
#    for el in row:
#        flat_weather_data.append(el)
# print(flat_weather_data)
#
# flat_weather_data = (el for row in weather_data for el in row)
# print(*flat_weather_data)
# print(type(flat_weather_data), sys.getsizeof(flat_weather_data))
#
# flat_weather_data = [el for row in weather_data for el in row if el > -10]
# print(*flat_weather_data)
# print(type(flat_weather_data), sys.getsizeof(flat_weather_data))


basket = ['apple', 'samsung', 'apple', 'huawei', 'asus', 'samsung']
unique_brands = [el for el in basket if basket.count(el) == 1]
print(unique_brands)  # ['huawei', 'asus']

unique_brands = set()
# print(dir(set))
tmp = set()
for el in basket:
    if el not in tmp:
        unique_brands.add(el)
    else:
        unique_brands.discard(el)
    tmp.add(el)
print(unique_brands)

unique_brands_ord = [el
                     for el in basket
                     if el in unique_brands]
print(unique_brands_ord)

chat_1 = {'user_1', 'user_5', 'user_7', 'user_8', 'user_11'}
chat_2 = {'user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'}

chats_common = chat_1 & chat_2
print(chats_common)  # {'user_1', 'user_7'}

chat_1_only = chat_1 - chat_2
chat_2_only = chat_2 - chat_1
print(chat_1_only)  # {'user_11', 'user_5', 'user_8'}
print(chat_2_only)  # {'user_9', 'user_10', 'user_2'}

both_chats = chat_1 | (chat_2)
print(both_chats)


import random

random_nums = {random.randint(1, 100) for _ in range(100)}
print(len(random_nums), random_nums)
