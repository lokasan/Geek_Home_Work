# Задание-1:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \
# матрицами \ светофор \ микроволновка

# Чем логичнее код тем лучше
import os
import time
from random import randint


class Tl:
    def __init__(self, light):
        if 1 <= light <= 3:
            self.light = light
            self.tl_mod = {1: "Зеленый", 2: "Желтый", 3: "Красный"}
            self.color = self.tl_mod[light]
            self.green_t = randint(30, 120)
            self.yellow_t = randint(3, 4)
            self.red_t = randint(30, 100)
        else:
            print("Ошибка")

    def green(self):
        for i in reversed(range(1, self.green_t + 1)):
            time.sleep(1)
            os.system("cls")
            print("зеленый\n", i)
        return "Желтый"

    def yellow(self):
        for i in reversed(range(1, self.yellow_t + 1)):
            time.sleep(1)
            os.system("cls")
            print("желтый\n", i)
        return "Красный"
    def red(self):
        for i in reversed(range(1, self.red_t + 1)):
            time.sleep(1)
            os.system("cls")
            print("красный\n", i)
        return "Зеленый"


print("Введите номер цвета, с которого начнет гореть светофор")
print("1 - Зеленый\n2 - Желтый\n3 - Красный")
light = int(input())
traffic_light = Tl(light)

while True:
    if traffic_light.color == "Зеленый":
        traffic_light.color = traffic_light.green()
    elif traffic_light.color == "Желтый":
        traffic_light.color = traffic_light.yellow()
    else:
        traffic_light.color = traffic_light.red()
