from typing import Self

class Point:
    def __init__(self, x, y, color = None):
        self.x = x
        self.y = y
        self.color = color # Задание-1: доработайте конструктор class Point для хранения цвета точки

    def distance(self, other_point: Self) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5 # Задание-1: реализуйте метод distance().x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5 # Задание-2: реализуйте метод distance()


# пример работы метода
p1 = Point(0, 0)
p2 = Point(0, 3)

result = p1.distance(p2)

# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

# TODO: your code here...
import math
def square (p1: Point, p2: Point, p3: Point) -> float:
    p = p1.distance(p2) + p2.distance(p3) + p3.distance(p1)
    return math.sqrt(p * (p - p1.distance(p2)) * (p - p2.distance(p3)) * (p - p3.distance(p1)))

color_list = set([p.color for p in points])

color_dict = {'red': 'красного', 'green': 'зеленого'}

for color in color_list:
    color_points = [p for p in points if p.color == color]
    print(f'Площадь {color_dict[color]} треугольника = {square(color_points[0], color_points[1], color_points[2])}')
