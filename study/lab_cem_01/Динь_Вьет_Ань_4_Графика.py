# Программа вычисляет таблицу значения функций и построить графику одной из них
# Начало, конец и шаг введятся с клавиатуры
# q1 = h**4-3*h**3+8*h**2-5
# q2 = e**(-h) +(h-1)*(h-1) - 3
# Оператор while
# Программа сделанна Динь Вьет Ань, группа ИУ7-14Б

from math import e, fabs

eps = 10**-6                         #Точность

st = float(input('Введите начало: '))
en = float(input('Введите конец: '))
step = float(input('Введите шаг: '))

print(chr(9484) + '-' * 68 + chr(9488))
print('|', '{:^10s}'.format('h'),
      '|', '{:^25s}'.format('q1'),
      '|', '{:^25s}'.format('q2'), '|')
print(chr(9500) + '-' * 68 + chr(9508))

s, t = 0, 1                          # Сумма и произведение вычисленных значений функции q2
h = st
while h - en <= eps:
    h = round(h, 5)
    q1 = h ** 4 - 3 * h ** 3 + 8 * h ** 2 - 5
    q2 = e ** (-h) + (h - 1) * (h - 1) - 3
    print('|', '{:^10.3g}'.format(h),
          '|', '{:^25.7g}'.format(q1),
          '|', '{:^25.7g}'.format(q2), '|')
    s += q1                                            # Вычисляет сумму вычисленных значений функции q1
    h += step
print(chr(9492) + '-' * 68 + chr(9496))
print()

print()
print('Графика функции q1:')
j = int(input("Введите количество засечек j (от 4 до 8): "))
while (j < 4) or (j > 8):
    print("J должен быть от 4 до 8")
    j = int(input("Введите количество засечек j снова: "))

mx = mn = round(s/(2/0.1+1), 2)                 # Вычислить минимальное и максимальное значения q1
                                                # Max и min равны среднему значению
h = st
while h - en < eps:
    h = round(h, 5)
    q1 = h ** 4 - 3 * h ** 3 + 8 * h ** 2 - 5
    if q1 - mx > eps:
        mx = q1
    if mn - q1 > eps:
        mn = q1
    h += step
    
# Шаг значения на оси Оу
d = (mx - mn)/(j - 1)
if mx - mn <= 10**-5:
    mx += 0.1

# Рисовать ось Оу
print(" "*10, end="")
k = 0
while k <= j:
    value = mn + k * d                          # Значения на оси Оу
    if abs(value) >= 10**4:
        print('{:7.7g}'.format(value), " "*11, end=" ")
    else:
        print('{:7.7g}'.format(value), " "*11, end=" ")
    k += 1
print(sep= ' ')
print('     x '+' '*8, end="")
k = 0
while k <= j:
    print(chr(9524)+chr(9472)*20, end="")
    k += 1
print()

# Построить графику функции q1
vtymax = int(round(16+21*(j-1), 0))                                   # Количество мест

# Если не нужно рисовать ось Ох
if (mn > eps) or (mx < eps):
    h = st
    while h - en <= eps:
        h = round(h, 5)
        q1 = h ** 4 - 3 * h ** 3 + 8 * h ** 2 - 5
        vty = int((q1-mn)/(mx-mn) * (vtymax-16))                       # Определить место точки
        print('{:8.4g}'.format(h) + 7 * " " + vty * ' ' + '*')         # Рисовать точку
        h += step

# Обратно
else:
    vt0 = int(round((-mn)/(mx-mn)*(vtymax-16), 0))                  # Мемто оси Оx
    do = (mx - mn) / (21 * (j - 1))                                 # Значение пустого места
    h = st
    while (h - en) <= eps:
        h = round(h, 5)
        q1 = h ** 4 - 3 * h ** 3 + 8 * h ** 2 - 5
        vty = int(round((q1-mn)/(mx-mn)*(vtymax-16), 0))            # Определить место точки
        if q1 < 0:
            if (-q1) < do:                                          # Точка лежит на ось Ох
                print('{:8.4g}'.format(h)+7*' ' + vt0 * ' ' + '*')
            else:                                                   # Точка слева от оси Ox
                print('{:8.4g}'.format(h)+7*" "+vty*' '+'*'+(vt0-vty-1)*' '+'|')
        if fabs(q1) <= eps:                                         # Точка лежит на ось Ох
            print("{:8.4g}".format(h)+7*" "+vty*" "+'*')
        if q1 > 0:
            if q1 < do:                                             # Точка лежит на ось Ох
                print('{:8.4g}'.format(h)+7*' '+vt0*' '+'*')
            else:                                                   # Точка справа от оси Ox
                print('{:8.4g}'.format(h)+7*' '+vt0*' '+ '|' +(vty-vt0-1)*' '+'*')
        h += step
