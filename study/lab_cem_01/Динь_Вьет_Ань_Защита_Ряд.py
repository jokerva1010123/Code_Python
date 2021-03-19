# Динь Вьет Ань, ИУ7-14Б
# Защита:
# y = 4*(1-1/3+1/5-....+(-1)**(n+1)/(2*n-1))

from math import fabs

eps = float(input('Введите точность: '))
step = int(input('Введите шаг печати: '))
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
	res1 = (-1)**(n+1)/(2*n-1)
	z += res1
	if (n-1)%step == 0:print('|', '{:^10g}'.format(n),
                                 '|', '{:^25.7g}'.format(res1*4),
                                 '|', '{:^25.7g}'.format(z*4), '|')
	n += 1
	if n==max_iter:
		break
print(chr(9492) + '-' * 68 + chr(9496))
print("Cумма: {:.10g}".format(z*4))
