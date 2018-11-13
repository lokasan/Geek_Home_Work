__author__ = 'Остроумов Борис Артемович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Решение:
#chislo = int(input("Введите целое число: "))
#while chislo>0:
#	print(chislo%10)
#	chislo//=10

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

#Решение:

#a = int(input("Введите значение первой переменной "))
#b = int(input("Введите значение второй переменной "))

#print("a = ", a)
#print("b = ", b)

#temp = a
#a = b
#b = temp
#print("Замена значений переменных:")
#print("a = ", a)
#print("b = ", b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Введите свой возраст: "))
access = 18;
if age < access:
	print("Извините, пользование данным ресурсом только с 18 лет!")
else:
	print("Доступ разрешен")