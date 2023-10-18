"""
Задача №2

Дан список чисел.
Выход:
Словарь, где в качестве ключа выступают цифры(0-9),
а в качестве значений список чисел,
в которых есть соответствующая цифра
Пример:
In: [56, 275, 642]
Out:
{ 2: [275, 642],
  4: [642],
  5: [56, 275]
  6: [56, 642]
  7: [275]
}
"""
import random as rnd
from pprint import pprint

rnd.seed(10)
# random.randint(n, k) возвращает число из интервала [n,k]
res1 = [rnd.randint(1, 1000) for _ in range(10)]

my_res = [str(x) for x in res1]

my_keys = []
for x in my_res:
    for y in x:
        if y not in my_keys:
            my_keys.append(y)

my_dict = {}
for n in my_keys:
    my_dict[n] = []

for a in my_res:
    for b in a:
        my_dict[(b[0])].append(a)

pprint(sorted(my_dict.items()))