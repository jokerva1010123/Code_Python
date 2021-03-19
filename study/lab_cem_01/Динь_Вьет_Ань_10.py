#Программа сделанна Динь Вьет Ань, ИУ7-14Б

#print menu
def menu():
    print('''\
        1. Выравнивание текста по левому краю.
        2. Выравнивание текста по правому краю.
        3. Выравнивание текста по ширине.
        4. Удаление заданного слова.
        5. Замена одного слова другим во всем тексте.
        6. Вычисление арифметического выражения.
        7. Найти предложение с максимальным количеством слов, начинающихся на заданную букву.
        0. Завершить программу
        '''
          )
#print text
def printtxt(text) :
    for ele in text :
        print(ele)
    print()

#Выравнивание текста по левому краю.
def alig_left(text):
    newtext = ['']*len(text)
    space = 1
    line = ''
    for i in range(len(text)):
        for ele in text[i] :
            if ele != ' ' :
                line += ele
                space = 0
            else :
                if space == 0 :
                    line += ele
                    space += 1
                else :
                    pass 
        newtext[i] = line
        line = ''    
    return(newtext)            

#Выравнивание текста по правому краю.
def alig_right(text):
    text = alig_left(text)
    maxline = 0
    newtext = ['']*len(text)
    for i in range(len(text)) :
        if len(text[i]) > maxline :
            maxline = len(text[i])
    for i in range(len(text)):
        newtext[i] = ' '*(maxline - len(text[i])) + text[i]
    return(newtext)

# Выравнивание текста по ширине.
def alig_width(txt, mlen):
    extxt = txt
    change_line = []
    add_probels = []
    probels = 0
    for el in txt:
        for letter in el:
            if letter == ' ':
                probels += 1
        add_probels.append(probels)
        probels = 0
    for i in range(len(txt)):
        if len(extxt[i]) != mlen:
            main_p = (mlen - len(txt[i])) // add_probels[i]
            dop_p = (mlen - len(txt[i])) % add_probels[i]
            for letter in txt[i]:
                if letter != ' ':
                    change_line.append(letter)
                else:
                    if dop_p != 0:
                        change_line.append(' ' * (main_p + 2))
                        dop_p -= 1
                    else:
                        change_line.append(' ' * (main_p + 1))
            extxt[i] = ''.join(change_line)
            change_line = []
    return extxt

# Удаление заданного слова.
def remove(text) :
    choice = input('Введите слово которое нужно удалить: ')
    choice = choice.upper()
    newtext = ['']*len(text)
    line = ''
    for i in range(len(text)):
        for el in text[i].split():
            element = el.upper()    
            if (element == choice or element == choice + ','
                    or element == choice + '.' or element == choice + '!'
                    or element == choice + '?'):
                if element != choice:
                    line += el[-1] + ' '
                else:
                    pass
            else:
                line += el + ' '
        newtext[i] = line
        line = ''
    return(newtext)

#Замена одного слова другим во всем тексте.
def replace(text) :
    while True:
        try:
            choice = input('Введите через пробел два слова:' +
                           ' сначала - то, что нужно заменить' + '\n').split()
            if len(choice) == 2:
                break
        except:
            print('Введите два слова через пробел!')
    st1 = choice[0].lower()
    newtext = ['']* len(text)
    line = ''
    for i in range(len(text)):
        for el in text[i].split():
            st2 = choice[1].lower()
            check = False
            if el[0].isupper() :
                check = True  
            element =  el.lower()   
            if (element == st1 or element == st1 + ','
                    or element == st1 + '.' or element == st1 + '!'
                    or element == st1 + '?'):
                if element != choice[0]:
                    line += st2 + element[-1] + ' '
                else:
                    if check :
                        line += st2[0].upper() + st2[1:] + ' '
                    else :
                        line += st2 + ' ' 
            else:
                line += el + ' '
        newtext[i] = line
        line = ''
    return(newtext)

#Вычисление арифметического выражения.
def calcu(text) :
    operations = ['+','-','*','/','**','//','(',')','%']
    cal_arr = []
    line = ''
    for i in range(len(text)):
        for el in text[i].split():
            for j in range(len(el)) :
                if el[j].isdigit() or el[j] in operations :
                    line += el[j]
        if line != '' :
            cal_arr.append(line) 
        line = ''   
    for i in range(len(cal_arr)):
        print(cal_arr[i],' = ',eval(cal_arr[i]))
    newtext = ['']*len(text)
    num = 0
    line = ''
    for i in range(len(text)) :
        for el in text[i].split():
            check = True
            for j in range(len(el)) :
                if el[j].isdigit() or el[j] in operations :   
                    check = False
                    break
            if not check :
                n = eval(cal_arr[num])
                line += str(n) +' '
                num += 1
            else :
                line += el +' '
        newtext[i] = line
        line = ''
    printtxt(newtext)  

#Найти предложение с максимальным количеством слов, начинающихся на заданную букву
def findSentenceWithMaxWord(text) :
    c = input('Введите начальную букву: \n')
    word = -1           # Максимальное количество слов, начинающихся на заданную букву.
    curWord = 0         # Максимальное количество слов, начинающихся на заданную букву в текущем предложении.
    sentence = []       # Предложения с максимальным количеством слов, начинающихся на заданную букву
    curSentence = ''    # Текущее предложение
    for x in text:
        for y in range(len(x)):
            if (x[y] == ' ' and x[y-1] != '.') or (x[y] != ' '):
                curSentence += x[y]
            if x[y] == '.':
                if word < curWord:
                    sentence = [curSentence]
                    word = curWord
                elif word == curWord:
                    sentence.append(curSentence)
                curSentence = ''
                curWord = 0
            if x[y-1] == ' ' and x[y] == c:
                curWord += 1
    if word == -1:
        print('Нет слов, начинающихся на заданную букву')
    else:
        for x in sentence:
            print(x)
    print()

text= [ 'They walked up the road together to the old man’s shack and went in through',
        'its open door. The old man leaned the mast with its wrapped sail',
        'against the wall. The boy put the box and the other gear',
        'beside it. The mast was nearly as long as the 2*(4-3)+1 room of',
        'the shack. The shack was made of the tough budshields of the',
        'royal palm. On the brown walls of the flattened, there was',
        'a picture. These were relics of his wife.' ]   

#main
maxlen = 0
for x in text:
    maxlen = max(maxlen, len(x))
printtxt(text)
while 1:
    menu()
    select = -1
    while (select < 0) or (select > 7) :
        select = int(input('Введите номер команды : '))

    if select == 1 :
        newtext = alig_left(text)
        printtxt(newtext)
    elif select == 2 :
        newtext = alig_right(text)
        printtxt(newtext)
    elif select == 3 :
        newtext = alig_width(text, maxlen) 
        printtxt(newtext)
    elif select == 4 :
        newtext = remove(text)
        printtxt(newtext)
    elif select == 5 :
        newtext = replace(text)
        printtxt(newtext)
    elif select == 6 :
        calcu(text)
    elif select == 7 :
        findSentenceWithMaxWord(text)
    elif select == 0 :
        break

    
