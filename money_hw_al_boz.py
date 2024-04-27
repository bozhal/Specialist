class Money: # класс для работы с денежными суммами
    def __init__(self, numb, dec):
        self.numb = numb
        self.dec = dec
        self.amount = self.numb * 100 + self.dec

        self.decimal = int(self.amount % 100)
        self.number = int((self.amount - self.decimal) // 100)

    def __str__(self):
        return f'{self.number}руб {self.decimal:02}коп'

    def __repr__(self):
        return str(self)

    def __add__(self, other): # *   сложение
        self.amount = self.amount + (other.amount)
        self.decimal = self.amount % 100
        self.number = self.amount // 100
        return Money(self.number, self.decimal)

    def __sub__(self, other): # *   вычитание
        self.amount = self.amount - other.amount
        if self.amount > 0:
            self.decimal = self.amount % 100
            self.number = self.amount // 100
        else: # НЕ ДОДЕЛАНО
            self.amount = abs(self.amount)
            self.decimal = self.amount % 100
            self.number = (self.amount - self.decimal) // 100
        return Money(self.number, self.decimal)

    def __mul__(self, other): # *   умножение на целое число
        self.amount = self.amount * other
        self.decimal = self.amount % 100
        self.number = self.amount // 100
        return Money(self.number, self.decimal)

    def __eq__(self, other): # *   сравнение (больше, меньше, равно, не равно)
        if self.amount == other.amount:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.amount - other.amount < 0:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.amount - other.amount > 0:
            return True
        else:
            return False

    def __mod__(self, other): # вычисление процента от суммы. %
        self.mod = round(self.amount * other / 100, 2)
        self.number = int(self.mod // 100)
        self.decimal = round(self.mod % 100, 2)
        return Money(self.number, self.decimal)

    def convert(self, currency): # Конвертация валют метод .convert("EUR")
        import requests
        import json
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        data_dict = json.loads(response.text)
        self.rate = data_dict['Valute'][currency]['Value']
        self.nominal = data_dict['Valute'][currency]['Nominal']
        self.conv = round((self.number * 100 + self.decimal) / self.rate * self.nominal, 2)
        self.number = int(self.conv // 100)
        self.decimal = round(self.conv % 100)
        return f'{self.number},{self.decimal}{currency} (rate={self.rate})'

# ==========================================================================================
# from functools import total_ordering
# Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
# __lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.#
#     @total_ordering
#     class Student:
#
#         def __eq__(self, other):
#             return self.last_name == other.last_name
#
#         def __lt__(self, other):
#             return self.last_name < other.last_name
# =========================================================================================
if __name__ == '__main__':
    money1 = Money(0, 30)
   # print(money1)
    money2 = Money(0, 70)
    # money3 = money1 + money2
    # print(money3)
    # money4 = money1 % 50
    # print(money4)
    # money5 = money4 * 2
    # print(money5)
    #
    # money6 = Money(1000, 0)
    # money7 = money6.convert("USD")
    # print(money7)
    money8 = money1 - money2
    print(money8, money8.amount, money8.number, money8.decimal)
