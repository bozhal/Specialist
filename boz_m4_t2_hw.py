"""
Задача №2
Напишите программу, определяющую количество уникальных символов в строке.
Вывести список символов и количество.

Например, в строке Hello, World! содержится десять
уникальных символов, а в строке zzz – один.
In: zzz
Out: [z], 1

In: Hello, World!
Out: ['H', ...., '!'], 10

!set еще не придумали
"""
stroka = "Hello, World!"
spisok = []
for s in stroka:
    if s not in spisok:
        spisok.append(s)
print(len(spisok))
