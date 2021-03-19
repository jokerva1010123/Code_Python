#Программа сделана Динь Вьет Ань, группа ИУ7-14Б
#Вычисление приближенного значения интеграла методом 3/8 и Буля

from math import sin, cos

# Вычесление значения производной
def f(x):
    return cos(x)
# Вычесление значения первообразной
def F(x):
    return sin(x)
# Вычисление интеграла методом 3/8
def Integral_38(n, start, end):
    if n % 3 != 0: return '—'
    E1 = 0
    E2 = 0
    h = abs(start - end) / n
    for i in range(1, int(n), 3):
        E1 += f(start + i * h)
        i += 1
        E1 += f(start + i * h)
    for i in range(3, int(n), 3):
        E2 += f(start + i * h)
    return 3 * h / 8 * (f(start) + f(end) + 3 * E1 + 2 * E2)
# Вычисление интеграла методом Буля
def boole(start, end, n):
    if n % 4: return '—'
    h = (end - start) / n
    summ = 0
    for i in range(1, n // 4 + 1):
        summ += (7 * f(start + h * (4 * i - 4)) +
                 32 *f (start + h * (4 * i - 3)) +
                 12 * f(start + h * (4 * i - 2)) +
                 32 * f(start + h * (4 * i - 1)) +
                 7 * f(start + h * 4 * i))
    summ *= 2 * h / 45
    return summ


a = float(input('Введите начало интегрирования: '))
b = float(input('Введите конец интегрирования: '))
n1 = int(input('Введите кол-во участков n1: '))
n2 = int(input('Введите кол-во участков n2: '))
# Точное значение интеграла
I_exact = F(b) - F(a)
I_38_n1 = Integral_38(n1, a, b)  # Интеграл, вычисленный методом 3/8 при n1
I_38_n2 = Integral_38(n2, a, b)  # Интеграл, вычисленный методом 3/8 при n2
I_boole_n1 = boole(a, b, n1)	# Интеграл, вычисленный методом Буля при n1
I_boole_n2 = boole(a, b, n2)	# Интеграл, вычисленный методом Буля при n2
# Вывод значений интегралов
print(f'\nМетод          n1 = {n1}           n2 = {n2}')
if n1 % 3 != 0 or n2 % 3 != 0:
    if n1 % 3 != 0:
        print('3/8            ' + I_38_n1, end='         ')
    else:
        print('3/8' + '{:22.7f}'.format(I_38_n1), end='')
    if n2 % 3 != 0:
        print('        ' + I_38_n2)
    else:
        print('{:18.7f}'.format(I_38_n2))
else:
    print('3/8' + '{:21.7f}'.format(I_38_n1) + '{:19.7f}'.format(I_38_n2))
if n1 % 4 != 0 or n2 % 4 != 0:
    if n1 % 4 != 0:
        print('Буля            ' + I_boole_n1, end='         ')
    else:
        print('Буля' + '{:22.7f}'.format(I_boole_n1), end='')
    if n2 % 4 != 0:
        print('        ' + I_boole_n2)
    else:
        print('{:18.7f}'.format(I_boole_n2))
else:
    print('Буля' + '{:21.7f}'.format(I_boole_n1) + '{:19.7f}'.format(I_boole_n2))
print(f'\nТочное значение: {I_exact}')
# ищем наименее точно вычисленный интеграл
d = 0
name = ['I_38_n1', 'I_38_n2', 'I_boole_n1', 'I_boole_n2']
value = [I_38_n1, I_38_n2, I_boole_n1, I_boole_n2]
I_not_exect_name = ''
I_not_exect = -1
for e in range(4):
    if value[e] == '—': continue
    if abs(I_exact - value[e]) > d:
        d = abs(I_exact - value[e])
        I_not_exect_name = name[e]    # в Integ_not_exect_name запоминаем наимен. наименее точного интеграла
        I_not_exect = value[e]     # в Integ_not_exect запоминаем значение наименее точного интеграла
abc = 1
if I_not_exect_name == 'I_38_n1':
    print(f'Наименее точный результат дал метод 3/8 при n1 = {n1}')
    k = n1;
elif I_not_exect_name == 'I_38_n2':
    print(f'Наименее точный результат дал метод 3/8 при n2 = {n2}')
    k = n2;
elif I_not_exect_name == 'I_boole_n1':
    print(f'Наименее точный результат дал метод Буля при n1 = {n1}')
    k = n1;
elif I_not_exect_name == 'I_boole_n2':
    print(f'Наименее точный результат дал метод Буля при n2 = {n2}')
    k = n2;
else:
    print('Методы не работают при n1 и n2')
    print('Метод 3/8 работает при n кратных 3')
    print('Метод Буля работает при n кратных 4')
    abc = 0
if abc:
    # Уточняем значение менее точного интеграла до точности eps
    method = 1 #1 - если метод 3/8, а 2 - если метод Буля дал значение наименее точного интеграла
    eps = float(input('Введите точность eps для уточнения значения интеграла: '))
    if I_not_exect_name == 'I_38_n1' or I_not_exect_name == 'I_38_n2':
        while abs(Integral_38(2 * k, a, b) - Integral_38(k, a, b)) > eps: k *= 2
    else:
        method = 2
        while abs(boole(a, b, 2*k) - boole(a, b, k)) > eps: k *= 2
    print(f'Точности eps удалось достичь при увеличении кол-ва участков до {k}')
    if method == 2:
        print('Вычисленное значение интеграла: ' '{:10.7f}'.format(boole(a, b, k)))
    else:
        print('Вычисленное значение интеграла: ' '{:10.7f}'.format(Integral_38(k, a, b)))
    print('Абсолютная погрешность: {:g}'.format(abs(I_exact - I_not_exect)))
    print('Относительная погрешность: {:g}'.format(abs((I_exact - I_not_exect) / I_exact)))
