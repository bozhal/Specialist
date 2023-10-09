"""
Задача №1.
Программа получает на вход последовательность из N целых чисел (от 2 до 10).

Вам нужно определить вид последовательности:
 - возрастающая
 - убывающая
 - случайная
 - постоянная

В качестве ответа следуют выдать прописными латинскими буквами тип последовательности:
1. ASCENDING (строго возрастающая)
2. WEAKLY ASCENDING (нестрого возрастающая, то есть неубывающая)
3. DESCENDING (строго убывающая)
4. WEAKLY DESCENDING (нестрого убывающая, то есть невозрастающая)
5. CONSTANT (постоянная)
7. RANDOM (случайная)

Примеры входных и выходных данных:
In: 119 4 2 -1  Out: DESCENDING
In: 3 8 8 11    Out: WEAKLY ASCENDING
In: 2 -1 7      Out: RANDOM
In: 5 5 5 5     Out: CONSTANT

Подсказка: используем функцию строки split()
"""
num = '5 5 5 5'
num = num.split()
new_num = []
for n in num:
    new_num.append(int(n))
flag = []

for x in range(1, len(new_num)):
    if new_num[x] - new_num[x - 1] > 0:
        f = "inc"
    elif new_num[x] - new_num[x - 1] == 0:
        f = "stable"
    elif new_num[x] - new_num[x - 1] < 0:
        f = "decr"
    flag.append(f)

ln = len(flag)

if flag.count("inc") == ln:
    print('ASCENDING')

elif flag.count("inc") + flag.count("stable") == ln and new_num[0] != new_num[-1]:
    print('WEAKLY ASCENDING')

elif flag.count("decr") == ln:
    print('DESCENDING')

elif flag.count("decr") + flag.count("stable") == ln and new_num[0] != new_num[-1]:
    print('WEAKLY DESCENDING')

elif flag.count("stable") == ln:
    print('CONSTANT')

else:
    print('RANDOM')