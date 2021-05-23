__author__ = 'Нестеренко Александр'
# Задание 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель
# между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во
# много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# 
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи
# 
# Задание 4.*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в
# новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
# 
# 
# Задание 5.**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать
# имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.


file_users = open('users.csv', 'r', encoding='utf-8')
user = file_users.readline()
file_hobby = open('hobby.csv', 'r', encoding='utf-8')
hobby = file_hobby.readline()

with open('users_hobby.txt', 'w', encoding='utf-8') as f:
    while user:
        if not hobby:
            hobby = None
            f.write(f'{user[:-1]}: {hobby}\n')
        else:
            f.write(f'{user[:-1]}: {hobby}')
        user = file_users.readline()
        hobby = file_hobby.readline()

# for line in file_users:
#    f.write(f'{line[:-1]}: {file_hobby.readline()}')
# # f.write(line2)
# users_hobby = open('users_hobby.txt', 'r', encoding='utf-8')
# users_hobby.close()
file_users.close()
file_hobby.close()
