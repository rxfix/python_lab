import urllib.request

response = urllib.request.urlopen(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

spammer_dic = {}
for line in response:
    line_ip = str(line).split(' - - ')[:1]  # ["b'173.255.199.22"]
    if spammer_dic.get(line_ip[0]):
        spammer_dic[line_ip[0]] += 1
    else:
        spammer_dic.setdefault(line_ip[0], 1)

max_request = 0
for key in spammer_dic:
    if spammer_dic[key] > max_request:
        max_request = spammer_dic[key]
        spammer_ip = key[2:]

print('IP адрес спамера:', spammer_ip, ', который сделал', max_request, 'запросов.')