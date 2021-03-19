#Программа сделана Динь Вьет Ань, группа ИУ7-14Б
#Вычислить матрицу F(n, m) по формуле F(x, y) = ln(u(x)) * v(y)
#Сформулировать вектор W, записав в нем суммы строк матрицы F в порядке убывания значения

from math import log

n = int(input('Введите количество строк n: '))
m = int(input('Введите количество столбцов m: '))
u = [float(x) for x in input('Введите n чисел массива u: ').split()]
v = [float(x) for x in input('Введите m чисел массива v: ').split()]
f = []
for x in range(n):
    a = [0]*m
    f.append(a)
for x in range(n):
    for y in range(m):
        f[x][y] = log(u[x]) * v[y]
print('Матрица F: ')
for x in range(n):
    for y in f[x]:
        print('{:^7.4g}'.format(y), end = ' ')
    print()
w = []
for x in range(n):
    a = sum(f[x])
    w.append(a)
w.sort(reverse = 1)
print('Вектор W: ')
for x in w:
    print('{:^7.4g}'.format(x), end = ' ')

