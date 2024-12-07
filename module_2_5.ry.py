def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Задайте количество строк матрицы :'))
m = int(input('Задайте количество столбцов матрицы   :'))
value = input(('Задайте значение матриц :'))
print('      '*m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Матрица пуста введите другое значение', n)
elif m <= 0:
    print('Матрица пуста ввидите другое значение', m)

    for i in matrix:
        print(*i)

n = int(input('Задайте количество строк матрицы :'))
m = int(input('Задайте количество столбцов матрицы   :'))
value = input(('Задайте значение матриц :'))
print('      '*m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Матрица пуста введите другое значение', n)
elif m <= 0:
    print('Матрица пуста ввидите другое значение', m)
    for j in matrix:
        print(*j)


n = int(input('Задайте количество строк матрицы :'))
m = int(input('Задайте количество столбцов матрицы   :'))
value = input(('Задайте значение матриц :'))
print('      '*m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Матрица пуста введите другое значение', n)
elif m <= 0:
    print('Матрица пуста ввидите другое значение', m)
    for k in matrix:
        print(*k)












