#Защита графики
#Построить графику функции y = cos(x) + 1
#Программа сделана Динь Вьет Ань, ИУ7-14Б

from math import cos, fabs

eps = 10**-7                         #Точность
st = float(input('Введите начало: '))
en = float(input('Введите конец: '))
step = float(input('Введите шаг: '))
j = int(input('Введите количество засечек j (от 4 до 8): '))
while (j < 4) or (j > 8):
    print('j должен быть от 4 до 8')
    j = int(input('Введите количество засечек j снова: '))
print('Графика функции у = сos(x) + 1: ')
mx, mn = -5, 5
x = st
while x - en < eps:
    x = round(x, 5)
    y = cos(x) 
    if y - mx > eps: mx = y
    if mn - y > eps: mn = y
    x += step
d = (mx - mn)/(j - 1)
print(' '*10, end='')
k = 0
while k <= j:
    value = mn + k * d 
    if abs(value) >= 10**4:
        print('{:7.7g}'.format(value),' '*11,end=' ')
    else:
        print('{:7.7g}'.format(value),' '*11,end=' ')
    k += 1
print()
print('     x '+' '*8, end='')
k = 0
while k <= j:
    print(chr(9524)+chr(9472)*20, end='')
    k += 1
print()
vtymax = int(round(16+21*(j-1), 0)) 
if (mn>eps) or (mx<eps):
    x = st
    while x-en<=eps:
        x = round(x, 5)
        y = cos(x) 
        vty = int((y-mn)/(mx-mn) * (vtymax-16))                      
        print('{:8.4g}'.format(x)+7*' '+vty*' '+ '*')        
        x += step
else:
    vt0 = int(round((-mn)/(mx-mn)*(vtymax-16), 0))                 
    do = (mx - mn) / (21 * (j - 1))                                
    x = st
    while (x - en) <= eps:
        x = round(x, 5)
        y = cos(x)
        vty = int(round((y-mn)/(mx-mn)*(vtymax-16), 0))          
        if y < 0:
            if (-y) < do:
                print('{:8.4g}'.format(x)+7*' ' + vt0 * ' ' + '*')
            else:                                                   
                print('{:8.4g}'.format(x)+7*" "+vty*' '+'*'+(vt0-vty-1)*' '+'|')
        if fabs(y) <= eps:                                         
            print("{:8.4g}".format(x)+7*" "+vty*" "+'*')
        if y > 0:
            if y < do:                                             
                print('{:8.4g}'.format(x)+7*' '+vt0*' '+'*')
            else:                                                   
                print('{:8.4g}'.format(x)+7*' '+vt0*' '+ '|' +(vty-vt0-1)*' '+'*')
        x += step
