#Программа сделана Динь Вьет Ань, группа ИУ7-14Б
#Из матрицы A(n, n) получить матрицу B(n, n-1) путем вычеркивания элементов главной диагонали
#В матрице В определить столбец с максимальным количеством положительных элементов

n = int(input('Введите размер n матрицы А: '))
a = []
for x in range(n):
    f = [int(x) for x in input('Введите элементы строки № {}: '.format(x+1)).split()]
    a.append(f)

print('Матрица А: ')
for x in range(n):
    for y in a[x]:
        print('{:^5} '.format(y), end = '')
    print()

for x in range(n):
    a[x].pop(x)
num = -1
col = []
for x in range(n-1):
    ans = 0
    for y in range(n):
        if a[y][x] > 0:
            ans += 1
    if ans > num:
        num = ans
        col = [x]
    elif ans == num:
        col.append(x)

print('Матрица В: ')
for x in range(n):
    for y in a[x]:
        print(y, end = ' ')
    print()
print('Столбец с максимальным количеством положительных элементов: ', end = '')
for x in col:
    print(x + 1, end = ' ')
print()
print('Количество положительных элементов: {:g}'.format(num))
