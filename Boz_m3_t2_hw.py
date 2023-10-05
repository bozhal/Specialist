"""
Задача №3
Дана строка из любых двух слов.
Поменяйте эти слова местами при выводе.

Пример:
In: 'Hello Python'
Out: 'Python Hello'

In: 'why not'
Out: 'not why'


Используем str.index(), срезы.
! Списки еще не придумали !
"""
slovo = 'Hello Python'
n = len(slovo)
i = 0
result = ''
while slovo[i] != ' ':
    result += slovo[i]
    i+=1
ostatok = slovo[len(result):]
print(result + ostatok)

