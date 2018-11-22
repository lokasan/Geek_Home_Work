def fibonacci(n, m):
    fib = [1, 1]
    i = 0
    while i < m:
        s = fib[i] + fib[i + 1]
        fib.append(s)
        i += 1
    return fib[n-1:m]


def sort_to_max(arr):
    i = 1
    while i < len(arr):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1
    return arr


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

n = int(input())
m = int(input())
print(fibonacci(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
