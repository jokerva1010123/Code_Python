# Программа сделанна Динь Вьет Ань, ИУ7 - 14Б
# Введите и проверить, является ли это числом
from sys import *
s = ''
while s != 'n':
    s = input()
    try:
        x = float(s)
        print('Это число')
    except:
        print('Это не число')
    ok, e, point = 1, 0, 0
    s = s.strip()
    for b in range(len(s)):
        a = s[b]
        if a > '9' or a < '0':
            if b == 0:
                if a != '+' and a != '-' and a != '.': ok = 0
                elif a == '.': point = 1
            else:
                if a != 'e' and a != 'E':
                    if a != '.':
                        if (a != '-' and a != '+') or ((a == '-' or a == '+') and (s[b-1] != 'e' and s[b-1] != 'E')): ok = 0
                    else:
                        if e == 1:
                            ok = 0
                            break
                        point += 1
                        ok = (point <= 1)
                else:
                    e += 1
                    ok = (e <= 1)
        if ok == 0: break
    print('Это ' + ['не ', ''][ok] + 'число')
