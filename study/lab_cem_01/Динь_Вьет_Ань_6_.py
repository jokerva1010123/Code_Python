# Программа сделана Динь Вьет Ань, ИУ7-14Б
""" Программа позволит с использованием меню:
1.Проинициализировать список первыми N элементами заданного ряда
2.Добавить элемент в произвольное место списка
3.Удалить произвольный элемент из списка
4.Очистить список
5.Найти значение K-го экстремума в списке, если он является списком чисел
6.Найти наиболее длинную убывающую последовательность отрицательных чисел, модуль которых является простым числом.
7.Найти последовательность, включающую в себя наибольшее количество элементов-строк, где гласных меньше, чем согласных """

from math import *
ko = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'I', 'U')
def check(po, lo = 0):
    try:
        if lo == 0: s = float(po)
        else: s = int(po)
        return 1
    except:
        return 0

b = []
while True:
    print('''\t1.Проинициализировать список первыми N элементами заданного ряда
        2.Добавить элемент в произвольное место списка
        3.Удалить произвольный элемент из списка
        4.Очистить список
        5.Найти значение K-го экстремума в списке, если он является списком чисел
        6.Найти наиболее длинную убывающую последовательность отрицательных чисел, модуль которых является простым числом.
        7.Найти последовательность, включающую в себя наибольшее количество элементов - строк, где гласных меньше, чем согласных
        0.Заверишить работу программы.\n''')
    
    a = input('Введите номер команды: ')
    if not check(a):
        print('Введите номер команды снова: ')
    elif int(a) == 0:
        print('Завершение работы.')
        break
    elif int(a) == 1:
        n = input('Введите положительное N: ')
        if check(n) and 0 < int(n):
            print('Введите n элементов: ')
            b = [x for x in input().split()]
        else:
            print('N не положительное число')
    elif int(a) == 2:
        val, x = input('Введите значение и место: ').split()
        if check(x):
            b.insert(int(x), val)
        else:
            print('Место не число')
    elif int(a) == 3:
        x = input('Место элемента: ')
        if check(x):
            if 0 <= int(x) < len(x):
                b.pop(int(x))
            else:
                print('Место не в списке')
        else:
            print('Место не число')
    elif int(a) == 4:
        b = []
    elif int(a) == 5:
        ok = 1
        for x in b:
            if not check(x):
                ok = 0
                break
        if ok == 0:
            print('Это не список чисел')
        else:
            ok = 0
            k = input('Введите число k: ')
            if not check(k):
                print('k не число')
                continue
            for x in range(1, len(b)-1):
                if float(b[x]) > float(b[x-1]) and float(b[x]) > float(b[x+1]):
                    ok += 1
                elif float(b[x]) < float(b[x-1]) and float(b[x]) < float(b[x+1]):
                    ok += 1
                if ok == int(k):
                    print('Значение {:g}-ого экстремума в списке: {:g}'.format(int(k), float(b[x])))
                    break
            if ok < int(k):
                print('Нет {:g}-ого экстремума в списке.'.format(int(k)))
    elif int(a) == 6:
        c = []
        ans = 0
        for x in b:
            if check(x, 1) and int(x) < 0:
                prime = True
                for i in range(2, int(sqrt(-int(x))) + 1):
                    if (-int(x)) % i == 0:
                        prime = False
                        break
                if prime:
                    while len(c) > 0 and c[-1] <= int(x):
                        c.pop(-1)
                    c.append(int(x))
                    ans = max(ans, len(c))
        print(ans)
    elif int(a) == 7:
        ans = ''
        g = cg = 0
        for x in b:
            if not check(x):
                for y in x:
                    if y in ko:
                        g += 1
                    elif 'a' <= y <= 'z' or 'A' <= y <= 'Z':
                        cg += 1
            if g < cg and len(x) > len(ans):
                ans = x
        print(ans)
    else:
        print("Введите команду из списка!")
