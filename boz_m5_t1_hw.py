"""
Задача №1

Написать программу, которая расшифрует строку,
используя набор букв из модуля string(string.ascii_lowercase),
Каждая символ - это две цифры.
Отчет с '00' -> 'a', '01' -> 'b' и до '25' -> 'z',
'26' - это пробел, он не входит в набор букв, нужно будет добавить
Вход: строка из цифр. Выход: Текст.

Используем словари.
Проверка работы программы выполняется через другую строку.

* реализовать и расшифровку и зашифровку
** реализовать через функции

Примеры строк:
'why not'
'how are you'
"""
code = '070411111426152419071413'

import string

letters = string.ascii_lowercase + " "
num = [f'{x:02}' for x in range(1,28)]
dict_l = dict(zip(num, letters)); dict_l
numb_to_read = [code [i:i+2] for i in range(0, len(numbers), 2)]
print(numb_to_read)
for n in numb_to_read:
    print(dict_l[n], end = '')

print('\n')

code2 = 'gdkknz oxsgnm01'
for value in code2:
    for keys in dict_l:
        if value in dict_l[keys]:
            print(keys,  end = '')