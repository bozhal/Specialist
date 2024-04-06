from __future__ import annotations
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point: Point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5  # Задание-1: реализуйте метод distance().x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5 # Задание-2: реализуйте метод distance()


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        p = self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)
        return math.sqrt(p * (p - self.p1.distance(self.p2)) * (p - self.p2.distance(self.p3)) * (p - self.p3.distance(self.p1)))


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание: 
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print("Периметр треугольника = ", triangle.perimeter())
print("Площадь треугольника = ", triangle.area())
