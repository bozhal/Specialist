
## Автомобиль
class Car: # Описать класс Car
# а) У машины должны быть атрибуты
  def __init__(self): # Значит должны быть значения по умолчанию
    self.gas = 0             # * "сколько бензина в баке" (gas)
    self.capacity = 10        # * "вместимость бака" - сколько максимум влезает бензина (capacity)
    self.gas_per_100km = 1   # * "расход топлива на 100 км" (gas_per_100km)
    self.mileage = 0        # * "пробег" (mileage)

# б) метод "залить столько-то литров в бак"
  def fill (self, amount): # должна учитываться вместительность бака
    if self.gas + amount <= self.capacity:
      self.gas = self.gas + amount
    else:           # если пытаемся залить больше, чем вмещается, то бак заполняется полностью +
      print(f'Лишние литры: {self.gas + amount - self.capacity}') # print'ом выводится сообщение о лишних литрах
      self.gas = self.capacity

# в) метод "проехать сколько-то км"
  def ride(self, distance):
    # в результате поездки потратится бензин и увеличится пробег.
    if self.gas < distance * self.gas_per_100km: # Если топлива не хватает на указанное расстояние,
      distance = self.gas * self.gas_per_100km   # едем пока хватает топлива.
    self.gas -= distance * self.gas_per_100km
    self.mileage += distance
    print(f'проехали {distance} километров') # выведет сообщение "проехали ... километров",

# г) реализовать метод: car1.info() (вывести количество бензина в баке и пробег)
  def info(self):
    print(f'количество бензина в баке: {self.gas} л,\nпробег: {self.mileage} км')

car1 = Car()
car1.info()
car1.fill(15)
car1.info()
car1.ride(20)
car1.info()
car1.fill(5)
car1.ride(3)
car1.info()