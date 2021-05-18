from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(content)


# def main(argv):
#     program, *args = argv
#     result = sum(map(int, args))
#     print(f'результат: {result}')
#
#     return 0
#
#
# if __name__ == '__main__':
#     import sys
#
#     exit(main(sys.argv))

import time

nums = []
for num in range(1, 10 ** 6 + 1):
   nums.append(num)

start = time.perf_counter()
nums_sum = 0
i = 0
while i < len(nums):
   nums_sum += nums[i]
   i += 1
finish = time.perf_counter()
print(nums_sum, finish - start, 'while')

start = time.perf_counter()
nums_sum = 0
for num in nums:
   nums_sum += num
finish = time.perf_counter()
print(nums_sum, finish - start, 'for in')


import datetime

datetime_1 = datetime.datetime(year=2020, month=12, day=5,
                              hour=18, minute=57, second=30)
datetime_2 = datetime.datetime(year=2020, month=1, day=1,
                              hour=0, minute=0, second=0)
datetime_delta = datetime_1 - datetime_2
print(datetime_delta.seconds)  # 68250
