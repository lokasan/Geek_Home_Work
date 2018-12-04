# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой
# треугольник нельзя создать и сделать exit(1)
import math


class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            print("Такой треугольник нельзя создать")
            exit(1)
        else:
            self.a = a
            self.b = b
            self.c = c

    def p(self):
        return self.a + self.b + self.c

    def s(self):
        p2 = (self.a + self.b + self.c) / 2
        s = math.sqrt(p2 * (p2 - self.a) * (p2 - self.b) * (p2 - self.c))
        return round(s)


tr = Triangle(5, 5, 1)
print("Площадь треугольника = ", tr.s())
print("Периметр треугольника = ", tr.p())
