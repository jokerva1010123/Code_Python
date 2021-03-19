# Динь Вьет Ань, ИУ7-14Б
# Задача:
# Вычислить сумму ряда с заданной точностью и вывести таблицу промежуточних значений c заданным шагом.
# Ряд: (-1)**n * (2*x)**(2*n)/factorial(2*n)

from math import factorial, fabs

print("(-1)**n * (2*x)**(2*n)/factorial(2*n)",end="\n\n")

x = float(input("Введите значение переменой x: ")) 
eps = float(input("Введите точность: ")) 
step = int(input("Введите шаг печати: ")) 
max_iter = int(input("Введите максимальное число итераций: ")) 

res1 = 0
res2 = float("inf")

z = 0

print(chr(9484) + '-' * 68 + chr(9488))
print('|', '{:^10s}'.format('N'),
      '|', '{:^25s}'.format('t'),
      '|', '{:^25s}'.format('z'), '|')
print(chr(9500) + '-' * 68 + chr(9508))

n = 1
while fabs(res1-res2)>=eps:
	res2 = res1
	res1 = (-1)**n * (2*x)**(2*n)/factorial(2*n)
	z += res1
	if (n-1)%step == 0:print('|', '{:^10g}'.format(n),
                                 '|', '{:^25.7g}'.format(res1),
                                 '|', '{:^25.7g}'.format(z), '|')
	n += 1
	if n==max_iter:
		break
print(chr(9492) + '-' * 68 + chr(9496))
print("Cумма: {:.10g}".format(z))


