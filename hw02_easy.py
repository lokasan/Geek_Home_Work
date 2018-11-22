
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Решение:

a = ["яблоко", "банан", "киви", "арбуз"]
c = 1
for i in a:
    print("{}{} {:>6}".format(c, ".", i))
    c += 1

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Решение

#a = ["ягода", "фрукт", "овощ", "гриб"]
#b = ["дыня", "фрукт", "гриб", "яблоня"]
#for i in b:
#    if i in a:
#        a.remove(i)
#print(a)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Решение

#a = [1, 45, 664, 7, 8, 9, 12, 14, 16, 18, 20, 22, 64, 128]
#b = []
#for i in a:
#    if i % 2:
#        b.append(i / 4)
#    else:
#        b.append(i * 2)
#print(a)
#print(b)
