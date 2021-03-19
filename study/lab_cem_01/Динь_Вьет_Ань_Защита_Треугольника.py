#Защита
#Программа сделана Динь Вьет Ань, ИУ7-14Б
#Ввести координаты вершин треугольника
#Ввести координаты одной точки и определить находиться ли внутри треугольника

from math import sqrt, fabs

eps = 10**-6

xa, ya = map(float, input('Введите координаты вершины А: ').split())
xb, yb = map(float, input('Введите координаты вершины B: ').split())
xc, yc = map(float, input('Введите координаты вершины C: ').split())

AB = sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))        #Вычисляет длину АВ
AC = sqrt((xa-xc)*(xa-xc) + (ya-yc)*(ya-yc))        #Вычисляет длину АС
BC = sqrt((xc-xb)*(xc-xb) + (yc-yb)*(yc-yb))        #Вычисляет длину ВС
if fabs(AB + AC - BC) <= eps or fabs(AB + BC - AC) <= eps or fabs(BC + AC - AB) <= eps:
    print('Это не треугольник')
else:
    xd, yd = map(float, input('Введите одной точки D: ').split())
    s = 1/2 *fabs((xc-xa)*(yb-ya) - (yc-ya)*(xb-xa))         #Вычисляет площадь треугольник ABC
    s1 = 1/2*fabs((xd-xa)*(yb-ya)-(yd -ya)*(xb-xa))          #Вычисляет площадь треугольник ABD
    s2 = 1/2*fabs((xd-xc)*(yb-yc)-(yd-yc)*(xb-xc))           #Вычисляет площадь треугольник BCD
    s3 = 1/2*fabs((xd-xa)*(yc-ya)-(yd-ya)*(xc-xa))           #Вычисляет площадь треугольник ACD
    #Если сумма 3 площадей треугольников равна площади основного треугольника, то точка лежит внутри, иначе - снаружи.
    if fabs(s - s1 - s2 - s3) <= eps:
        print('Точка находится внутри треугольника')
    else:
        print('Точка не находится внутри треугольника')
