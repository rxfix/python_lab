# import urllib.request
#
# from requests import get
# import sys
#
# # file_1 = open('hello.txt', 'r', encoding='utf-8')
# # # content = file_1.read()
# # # print(content)
# #
# # # clean_content = content.replace('\n', ' ').replace('\r', ' ')
# # # print(clean_content)
# #
# # # paragraphs = content.splitlines()
# # # print(paragraphs)
# #
# # for line in file_1:
# #    print(line)
# # file_1.close()
#
# # response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
# # content = response.content.decode(
# #         encoding=response.encoding)
# # print(response.text)
#
# response = urllib.request.urlopen(
#     'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

# line = response.readline()
# print(line)
# line = response.readline()
# print(line)
# line = response.readline()
# print(line)
# line = response.readline()
# print(line)


# def main(argv):
#    program, *args = argv
#    result = sum(map(int, args))
#    print(f'результат: {result}')
#
#    return 0
#
#
# if __name__ == '__main__':
#    import sys
#
#    exit(main(sys.argv))
