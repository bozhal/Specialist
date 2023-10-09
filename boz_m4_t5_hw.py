"""
Задача №5.
Написать программу, используя набор букв из модуля string(string.ascii_lowercase).

Вход: размер шахматной доски(NxN), где N от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Подсказка: Используем вложенные циклы

Пример:
In: 4
Out:
    a4 b4 c4 d4
    a3 b3 c3 d3
    a2 b2 c2 d2
    a1 b1 c1 d1
"""
import string
n = 4
rng = string.ascii_lowercase

for x in range(n):
    for y in range (n):
        f = rng[y]
        s = n - x
        print(f'{f}{s} ', end = '')
    print('')