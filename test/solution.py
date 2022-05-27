from itertools import product
import random

'''
Каков алгоритм:
Так как у нас в исходном числе уже могут быть цифры, можно сказать,
что мы фиксируем эти самые цифры, выкидывая ненужные комбинации.
Пример:
300? - в этом числе будет всего девять комбинаций: от 3000 до 3009
?01 - тут комбинации от 001 до 901
??1 - тут от 00 до 991
и т. д.

'''
numbers = '0123456789'

with open('input.txt', 'r') as f:
    items = f.read().split('\n')

for i in range(len(items)):
    # здесь будут конечные массивы с числами A, B, C

    item = items[i]
    A_list = []
    B_list = []
    C_list = []

    # избавляемся от арифметических операций
    item = item.replace('+', '__').replace('=', '__')
    item = item.split('__')
    
    A, B, C = item[0], item[1], item[2]

    # три одинаковых цикла, мы избавляемся от вопросиков и делаем их чиселками
    for x in product(numbers, repeat=A.count('?')):
        a = A
        for i in x:
            a = a.replace('?', i, 1)
        A_list.append(a)

    for x in product(numbers, repeat=B.count('?')):
        b = B
        for i in x:
            b = b.replace('?', i, 1)
        B_list.append(b)

    for x in product(numbers, repeat=C.count('?')):
        c = C
        for i in x:
            c = c.replace('?', i, 1)
        C_list.append(c)

    # избавляемся от шелухи и сортируем массивы
    A_list = sorted(set(A_list))
    B_list = sorted(set(B_list))
    C_list = sorted(set(C_list))

    # пора складывать чиселки, но нужно не забывать о лидирующих нулях
    ans = []
    for a in A_list:
        for b in B_list:
            remember = abs(len(a) - len(b))  # не забываем о нулях!!!
            if (summ := '0' * remember + str(int(a) + int(b))) in C_list:  # использузем моржа
                ans.append(str(f'{a}+{b}={summ}'))
            else:
                ans.append('impossible')

    '''
    Здесь, пожалуй, поясню. Нам не нужны дублирующиеся решения. Потому мы их отбросим.
    Если даже массив решений целиком состоит из импоссиблов, это ничего не меняет.
    '''
    ans = list(set(ans))
    if not all(x == 'impossible' for x in ans):
        ans.remove('impossible')
    # если в массиве есть нерабочие решения, НО ЕСТЬ
    # НОРМАЛЬНЫЕ, мы просто отбрасываем импоссибл
    print(ans)

    index = random.randint(0, len(ans) - 1)

    '''
    Здесь финальный штрих - я не знаю, как идёт у Вас проверка, 
    файлом или ручным вводом, я решил сделать в append-режиме вывод файла,
    так как при 'w' программа просто пересоздаёт файл при новой итерации в этом цикле, 
    удаляя предыдущее решение, а при append оно точно сохраняется.
    '''

    with open('output.txt', 'a') as file: 
        print(ans[index], file=file)  # вытаскиваем случайный(!!!) элемент из массива, как сказано по условию задачи

    ans = []  # ну и очищаем массив для последующих итераций

    '''
    В целом, задача несложная, но неприятна тема с выводом в файл.
    '''
