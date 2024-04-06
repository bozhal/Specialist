class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
# Считаем, что точек с одинаковыми координатами у нас нет.

# TODO: your code here...
max_dist = 0
point_zero = Point(0, 0)
for point in points:
    dist = distance(point_zero, point)
    if dist > max_dist:
        max_dist = dist


print("Координаты наиболее удаленной точки = ", max_dist)


