# Определить коодинаты новой точки, чтобы построить равнобедренный треугольник
# Программа сделанна Динь Вьет Ань, группа ИУ7-14Б

from math import sqrt, fabs

xa, ya = map(int, input('Введите координаты вершины А: ').split())
xb, yb = map(int, input('Введите координаты вершины B: ').split())
xc, yc = map(int, input('Введите координаты вершины C: ').split())

AB = sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))        # Вычисляет длину АВ
AC = sqrt((xa-xc)*(xa-xc) + (ya-yc)*(ya-yc))        # Вычисляет длину АС
BC = sqrt((xc-xb)*(xc-xb) + (yc-yb)*(yc-yb))        # Вычисляет длину ВС

if fabs(AB - AC + BC) <= 10**-8 or fabs(AB + AC - BC) <= 10**-8 or fabs(BC + AC - AB) <= 10**-8:
    print('Это не треугольник')
else:
    # Треугольник с двумя равными сторонами - это равнобедренный треугольник
    if fabs(AB - AC) <= 10**-8 or fabs(AB - BC) <= 10**-8 or fabs(BC - AC) <= 10**-8:
        print('Треугольник равнобедренный')
    else:
        AM = sqrt((2 * (AB * AB + AC * AC) - BC * BC) / 4)              # Вычисляет медиану AМ
        CP = sqrt((2 * (AC * AC + BC * BC) - AB * AB) / 4)              # Вычисляет медиану СP
        BN = sqrt((2 * (AB * AB + BC * BC) - AC * AC) / 4)              # Вычисляет медиану BN
        s = 1 / 2 * abs((xc - xa) * (yb - ya) - (yc - ya) * (xb - xa))  # Вычисляет площадь треугольник ABC
        da = sqrt(AM * AM - (2 * s / BC)*(2*s/BC))                      # Вычисляет росстояние от А до новой точки
        db = sqrt(BN * BN - (2 * s / AC)*(2*s/AC))                      # Вычисляет росстояние от B до новой точки
        dc = sqrt(CP * CP - (2 * s / AB)*(2*s/BC))                      # Вычисляет росстояние от C до новой точки
        if fabs(min(min(da, db), dc) - da) <= 10**-8:
            if AB > AC:
                x = xa + (da/BC) * (xc - xb)
                y = ya + (da/BC) * (yc - yb)
            else:
                x = xa - (da/BC) * (xc - xb)
                y = ya - (da/BC) * (yc - yb)
            print('Координаты новой точки: {:g}, {:g}'.format(x, y))
        elif fabs(min(min(da, db), dc) - db) <= 10**-8:
            if BC > AB:
                x = xb + (db/AC) * (xc - xa)
                y = yb + (db/AC) * (yc - ya)
            else:
                x = xb - (db/AC) * (xc - xa)
                y = yb - (db/AC) * (yc - ya)
            print('Координаты новой точки:2 {:g}, {:g}'.format(x, y))
        else:
            if BC > AC:
                x = xc + (dc/AB) * (xb - xa)
                y = yc + (dc/AB) * (yb - ya)
            else:
                x = xc - (dc/AB) * (xb - xa)
                y = yc - (dc/AB) * (yb - ya)
            print('Координаты новой точки:3 {:g}, {:g}'.format(x, y))
