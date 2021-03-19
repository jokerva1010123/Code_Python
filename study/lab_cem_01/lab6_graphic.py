#Опратор (for)

#Определить также разность между максимальным и минимальным значением С

#s-Общее значение функции C от i = -1 до i = 1
#i-Бегущая переменная
#a-Переменная
#c-Функция
#maxc,minc-Максимальное и минимальное значение С

import math

m=float(input("Введите начальное значение M: "))
while ((m<-1000) or (m>1000)):
    print("M должно быть в [-1000,1000]")
    m=int(input("Введите начальное значение M снова: "))
n=float(input("Введите конечное значение N: "))
while ((n>1000) or (n<=m)):
    print("N должно быть больше M и в (-1000,1000]")
    n=int(input("Введите конечное значение N снова: "))
i=float(input("Введите диапазон изменения переменной i: "))
while (i>(n-m)):
    print("I должен быть меньше или равен (N-M)")
    i=float(input("Введите диапазон изменения переменнойi снова: "))
j=int(input("Введите количество засечек j (от 4 до 8): "))
while ((j<4) or (j>8)):
    print("J должен быть от 4 до 8")
    j=int(input("Введите количество засечек j снова: "))
print("\n")
s=0
for a in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    a=round(a/10**7,4)
    c=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
    s+=c
maxc=minc=round(s/((n-m)/i+1),2)
for a in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
    a=round(a/10**7,4)
    c=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
    if c>maxc: maxc=round(c,2)
    if c<minc: minc=round(c,2)
d=(maxc-minc)/(j-1)
print(" "*10,end="")
for k in range(0,j):
    l=minc+k*d
    if (abs(l)>=10**4):
            print("{:5.2e}".format(l)," "*10,end=" ")
    else: print("{:6.2f}".format(l)," "*14,end=" ")
print(sep=" ")
print("     x "+" "*8,end="")
for k in range(0,j):
    print(chr(9524)+chr(9472)*20,end="")
print(sep=" ")
vtymax=int(round(16+21*(j-1),0))
x0=(-minc)/(maxc-minc)
vt0=int(round(x0*(vtymax-16),0))
if vt0==0: vt0+=1
do=(maxc-minc)/(21*(j-1))
if ((minc>0) or (maxc<0)):
    for a in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
        a=round(a/10**7,4)
        c=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
        x=(c-minc)/(maxc-minc)
        vty=int(x*(vtymax-16))
        print("{:8.2f}".format(a)+7*" "+vty*" "+"*")
else:
    for a in range(round(m*10**7),round(n*10**7+1),round(i*10**7)):
        a=round(a/10**7,4)
        c=a**7-a**6+8*a**5-4*a**4+6*a**3+2*a**2-5*a+1
        x=(c-minc)/(maxc-minc)
        vty=int(round(x*(vtymax-16),0))
        if (c<0):
            if (-c)<do:
                print("{:8.2f}".format(a)+7*" "+(vt0)*" "+"*")
            else:
                print("{:8.2f}".format(a)+7*" "+vty*" "+"*"+(vt0-vty-1)*" "+(chr(9474)))
        if (c==0):
            print("{:8.2f}".format(a)+7*" "+vty*" "+("*"))
        if (c>0):
            if (c<do):
                print("{:8.2f}".format(a)+7*" "+vt0*" "+"*")
            else:
                print("{:8.2f}".format(a)+7*" "+vt0*" "+(chr(9474))+(vty-vt0-1)*" "+"*")
print("\nРазработал Чыонг Нгуен Вьет Уи. ИУ7И-12Б")
