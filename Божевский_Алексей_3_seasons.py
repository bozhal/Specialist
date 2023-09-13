# Времена года
month = int(input('Введите номер месяца  '))
if  month == 12 or month < 3 :
    s = "WINTER" 
elif 2 < month < 6:
    s = "SPRING"
elif 5 < month < 9:
    s = "SUMMER"
else :
    s = "AUTUMN"
print(s)