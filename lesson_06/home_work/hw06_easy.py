# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
"""
import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
#поиск длин сторон:
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)
#поиск периметра:
    def perimetr(self):
        self.perimetr = (self.AB + self.BC + self.CA)
        return (self.perimetr)
#поиск площади:
    def ploshad(self):
        self.perimetr /=2
        self.ploshad =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB)*(self.perimetr - self.BC)* (self.perimetr - self.CA)),2)
        return (self.ploshad)
#поиск высоты:
    def vysota(self):
        self.ploshad *=2
        self.vysota =  round((self.ploshad / self.CA),2)
        return (self.vysota)
my_tri = Triangle (2,2,5,8,7,4)
print('Длинна строны АВ = {}, ВС = {}, СA = {}' .format(my_tri.AB, my_tri.BC,my_tri.CA))
print('Периметр треугольника АВС равен {}'.format(my_tri.perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_tri.ploshad()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_tri.vysota()))

"""
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt
class HipsTrapez:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        #вычисляем длину сторон трапеции
        self.length1 = float(((self.point2[0] - self.point1[0] ** 2 + self.point2[1] - self.point1[1]) ** 2) ** (1 / 2))
        self.length2 = float(((self.point3[0] - self.point2[0] ** 2 + self.point3[1] - self.point2[1]) ** 2) ** (1 / 2))
        self.length3 = float(((self.point3[0] - self.point4[0] ** 2 + self.point3[1] - self.point4[1]) ** 2) ** (1 / 2))
        self.length4 = float(((self.point1[0] - self.point4[0] ** 2 + self.point1[1] - self.point4[1]) ** 2) ** (1 / 2))
        #вычисляем диагональ
        self.diagonal1 = float(((self.point3[0] - self.point1[0]) ** 2 + (self.point3[1] - self.point1[1]) ** 2) ** (1 / 2))
        self.diagonal2 = float(((self.point4[0] - self.point2[0]) ** 2 + (self.point4[1] - self.point2[1]) ** 2) ** (1 / 2))
        print("Длина трапеции: ", self.length1, self.length2, self.length3, self.length4)
        print("Длина диагонали: ", self.diagonal1, self.diagonal2)
    def check_hips(self):
        if self.length1 == self.length3:
            if self.diagonal1 == self.diagonal2:
                res = "Равнобедренная трапеция"
            else:
                res = "Не равнобедренная трапеция"
            return res
    #периметр

    def perimeter(self):
        return self.length1 + self.length2 + self.length3 + self.length4
    #площадь трапеции

    def square(self):
        if self.length1 == self.length3 and self.length2 != self.length4:
            a = (abs (self.length2 - self.length4))/2
            h = sqrt((self.length1**2) - a**2)
            return h*(self.length2 + self.length4)/2
        else:
            print("это не равнобедренная трапеция")
#пример равнобедренной трапеции
trap1 = HipsTrapez([0, 0], [1, 4], [5, 4], [6, 0])
print(trap1.check_hips(), "Периметр: ", trap1.perimeter(), "Площадь: ", trap1.square())





