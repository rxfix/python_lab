import sys
print('show_sales.py')
if len(sys.argv) < 2 :
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(str.strip(line))