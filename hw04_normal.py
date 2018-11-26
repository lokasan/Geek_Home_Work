import random
from itertools import groupby


def matrix(n):
    matr = [[random.randint(1, 100) for j in range(n)] for i in range(n)]
    for row in range(len(matr)):
        matr[row][random.randint(0, n - 1)] = 0
        for col in range(len(matr[row])):
            print(f"{matr[row][col]:2}", end=" ")
        print()

def read_file():
    f = open("data.txt", "r")
    data = f.readline()
    return max((list(j) for i, j in groupby(data)), key=len)


def write_file():
    f = open("data.txt", "w")
    string = ""
    for i in range(2500):
        number = random.randint(0, 9)
        string += str(number)
    f.write(string)
    f.close()
    return read_file()


# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random

print(write_file())

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные элементы тоже рандомные. Пользователь вводит размер

n = int(input("Введите размер матрицы: "))
matrix(n)
