#Опреределить решения квадратного управления
#Программа сделанна Динь Вьет Ань с группы ИУ7-14Б("Hello world")

from math import sqrt

print('Решиние квадратного уравления')

a, b, c = map(float, input('Ведите a, b, c: ').split())

if a == 0:                                  
    if b == 0:
        if c == 0:
            print('x - любое число')         #a = b = c = 0, любое
        else:
            print('Нет решений')             #a = b = 0, c != 0, нет решений
    else:   
        x = -c/b                             #bx + c = 0(прямая)
        print('x = {:g}'.format(x))       

else:                                        #a != 0, квадратное управление
    D = b*b - 4*a*c                          #Вычисляет дискриминант
    if D > 0:                                
        x1 = (-b+sqrt(D))/(2*a)              #Дискриминант > 0, то 2 решения
        x2 = (-b-sqrt(D))/(2*a)
        print('x1 = {:g}'.format(x1))
        print('x2 = {:g}'.format(x2))
    elif D == 0:
        x = -b/2*a                          #Дискриминант == 0, то 1 решение
        print('x = {:g}'.format(x))         
    else:                                   
        print('Нет решений')                #Дискриминант < 0, нет решений
