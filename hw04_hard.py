# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.


from collections import Counter


def matr(n):
    st, m = 1, 0
    matr = [[0 for j in range(n)] for i in range(n)]
    if n % 2:
        matr[n//2][n//2] = n*n
    for v in range(n // 2):
            # Заполнение левой вертикальной матрицы
        for i in range(n - m):
            matr[i + v][v] = st
            st += 1
            # Заполнение нижней горизонтальной матрицы
        for i in range(v + 1, n - v):
            matr[-v - 1][i] = st
            st += 1
            # Заполнение правой вертикальной матрицы
        for i in range(v + 1, n - v):
            matr[-i - 1][-v - 1] = st
            st += 1
            # Заполнение верхней горизонтальной матрицы
        for i in range(v + 1, n - (v + 1)):
            matr[v][-i - 1] = st
            st += 1
        m += 2
    for row in range(len(matr)):
        for col in range(len(matr[row])):
            print(f"{matr[row][col]:2}", end=" ")
        print()


def read_file():
    f = open("pwd.txt", "r")
    data = f.read()
    data = data.replace(";", " ").replace("\n", " ")
    data = data.split()
    i = 0
    while i < len(data):
        del data[i]
        i += 1
    top = Counter(i for i in data)
    return top.most_common(10)

# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами


print(read_file())
n = int(input("Введите размер матрицы: "))
matr(n)
