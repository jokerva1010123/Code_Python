# Программа сделана Динь Вьет Ань, ИУ7-14Б
'''
Программа позволит с использованием меню:
0. Завершить программу
1. Ввод строки.
2. Настройка шифрующего алгоритма.
3. Шифрование строки, используя шифр Виженера.
4. Расшифровывание строки
'''

ko = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'I', 'U')
def check(po, lo = 1):
    try:
        if lo == 0: s = float(po)
        else: s = int(po)
        return 1
    except:
        return 0

s = ''
key = ''
ans = []
while 1:
    print(
    '''\
    0. Завершить программу.
    1. Ввод строки.
    2. Настройка шифрующего алгоритма.
    3. Шифрование строки, используя шифр Виженера.
    4. Расшифровывание строки.
    '''
    )
    a = input('Введите номер команды: ')
    if not check(a):
        print('Введите номер команды снова: \n')
    elif int(a) == 0:
        print('Завершение работы.')
        break
    elif int(a) == 1:
        s = input('Введите сторку: ')
    elif int(a) == 2:
        key = input('Введите кодовое слово: ')
    elif int(a) == 3:  
        if key == '':
            print('Нет кодового слова.')
        elif s == '':
            print('Нет строки для шифрования.')
        else:
            ans = []
            for x in range(len(s)):
                if s[x] != ' ':
                    if s[x].islower():
                        ans.append(chr((ord(s[x])-ord('a') + ord(key[x%len(key)].lower()) - ord('a'))%26+ord('a')))
                    else:
                        ans.append(chr((ord(s[x])-ord('A') + ord(key[x%len(key)].lower()) - ord('a'))%26+ord('A')))
                else:
                    ans.append(' ')
            print(''.join(ans), '\n')
    elif int(a) == 4: 
        if key == '':
            print('Нет кодового слова.')
        elif s == '':
            print('Нет строки для расшифрования.')
        else:
            ans = []
            for x in range(len(s)):
                if s[x] != ' ':
                    if s[x].islower():
                        ans.append(chr((ord(s[x])-ord('a') - ord(key[x%len(key)].lower()) + ord('a')+26)%26+ord('a')))
                    else:
                        ans.append(chr((ord(s[x])-ord('A') - ord(key[x%len(key)].lower()) + ord('a')+26)%26+ord('A')))
                else:
                    ans.append(' ')
            print(''.join(ans), '\n')
    else:
        print("Введите команду из списка!\n")

