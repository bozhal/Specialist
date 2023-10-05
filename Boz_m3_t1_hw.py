"""
Задача №2
Дано слово из символов(латинские буквы + цифры), других нет.
Нужно вывести новой строкой только цифры, если они есть или
написать, что их нет.
Пример:
In: 'antuh1ouou21au3'
Out: 1213

In: 'sauhsauhasnhuasnhu'
Out: 'no digits'

Подсказки, что использовать:
while, индексация для элементов строки, str.isdigit()
"""
import string as st
slovo = 'sauhsauhasnhuasnhu'
n = len(slovo)
i = 0
result = ''
while i < n:
    if slovo[i] in st.digits:
        result += slovo[i]
    i+=1
if result == '':
    result = 'no digits'
print(result)