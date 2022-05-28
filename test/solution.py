from itertools import product
import random

'''
    Каков алгоритм:
    Так как у нас в исходном числе уже могут быть цифры, можно сказать,
    что мы фиксируем эти самые цифры, выкидывая ненужные комбинации.
    Пример:
    300? - в этом числе будет всего девять комбинаций: от 3000 до 3009, 300 фиксируется
    ?01 - тут комбинации от 001 до 901, 01 фиксированы
    ??1 - тут от 001 до 991, единица фиксирована
    и т. д.
    
    P.S.: получилось слишком много комментариев. Слишком...
'''


numbers = '0123456789'

with open('input.txt', 'r') as f:
    items = f.read().split('\n')

answers = []

for i in range(len(items)):
    #  здесь будут конечные массивы с числами, которые соответствуют возможным комбинациям A, B, C

    item = items[i]
    A_list = []
    B_list = []
    C_list = []

    #  избавляемся от арифметических операций
    item = item.replace('+', '__').replace('=', '__')
    item = item.split('__')
    
    A, B, C = item[0], item[1], item[2]

    #  три одинаковых цикла, мы избавляемся от вопросиков и делаем их чиселками
    #  итерируемся по количеству найденых вопросов
    #  пример: в ?0? найдено 2 вопроса
    #  значит мы будем итерироваться по ('0', '0'), ('0', '1') и так до ('9', '9')
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

    # пора складывать чиселки, но нужно не забывать о лидирующих нулях, ибо формат ответа требует наличие лидирующих нулей
    ans = []
    for a in A_list:
        for b in B_list:
            max_len = max(len(a), len(b), len(c))  # берем максимальную длину одного из чисел, дабы нули не потерять
            if (summ := str(int(a) + int(b))) in C_list:  # использузем моржа, чтобы не считать сумму снова и чтобы запихнуть в ответ
                a = '0' * (max_len-len(a)) + a # приписываем столько нулей, сколько нам не хватает в числе
                b = '0' * (max_len-len(b)) + b
                ans.append((f'{a}+{b}={summ}')) # сумме нули не приписываем, ибо она всегда больше или равна длине одного из (A, B)
            else:
                ans.append('impossible')

    '''
    Здесь, пожалуй, поясню. Нам не нужны дублирующиеся значения в массиве 
    (их не будет, но я это для impossible-ов делаю это скорее). 
    Потому мы их отбросим.
    Если даже массив решений целиком состоит из импоссиблов, это ничего не меняет.
    '''
    
    ans = list(set(ans))
    if not all(x == 'impossible' for x in ans):
        ans.remove('impossible') # а это мы делаем, чтобы случайно не вывести impossible в случае, когда у примера могут быть решения

    #  если в массиве есть нерабочие решения, НО ЕСТЬ
    #  НОРМАЛЬНЫЕ, мы просто отбрасываем импоссибл - в противном случае у нас ВООБЩЕ нет решений

    print(ans) #  для себя выводим список ответов
    answers.append(ans)

    ans = []  #  очищаем массив для последующих итераций

with open('output.txt', 'w') as filo:
    for it in answers:
        index = random.randint(0, len(it) - 1)
        print(it[index], file=filo)

    '''
    В целом, задача несложная, но неприятна тема с обработкой.
    Неприятны лидирующие нули. Неприятен дедлайн :D
    '''
