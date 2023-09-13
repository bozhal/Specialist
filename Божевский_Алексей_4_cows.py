# Cows
n = int(input('Введите количество коров  '))
ending = n % 10
ending2 = n % 100

if ending == 1 and not(10 < ending2 < 15) :
    en = (str("а"))
  
elif 1 < ending < 5:
    en = (str("ы"))

else : 
    en = (str(""))
    
n = str(n)
print("На лугу пасется " + n + " коров" + en)