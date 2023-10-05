"""
Задача №4
Строка из нескольких слов, не более 10.
Знаки препинания не используем.
Определите, сколько букв содержит самое длинное слово в строке.

Примеры:
In: Как дела в учебе
Out: 5

In: Закрепляем циклы в Питоне
Out: 10

In: Цикл while уже придумали а списки еще нет
Out: 9

Цикл while уже придумали, а списки еще нет!!!
"""
# in progress
slovo = 'Как дела в учебе'
n = len(slovo)
i = 0
result = 0
last = 0
while i < n:
        if slovo[i] == ' ':
            lenth = i - last
            if lenth > result:
                result = lenth
            last = i
        if i == n-1:
            lenth = i - last
            if lenth > result:
                result = lenth
        i += 1

print(result)