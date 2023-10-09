"""
Задача №3
Дана строка.
Необходимо посчитать количество вхождений каждого символа.

Пример:
In: Hello, Python1.
Out:
H: 1
e: 1
h: 1
l: 2
o: 2
,: 1
P: 1
y: 1
t: 1
n: 1
1: 1
 : 1
.: 1
"""

# not completly 
stroka = "Hello, Python1."
spisok = []
for s in stroka:
    if s not in spisok:
        spisok.append(s)
for ch in spisok:
    v = stroka.count(ch)
    print(f'{ch}:{v}')