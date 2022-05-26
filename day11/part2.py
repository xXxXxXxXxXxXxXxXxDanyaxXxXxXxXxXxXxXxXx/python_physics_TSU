import string

# импортируем англ. алфавит и создаем массив удвоений (нам нужно по задаче)
alphabet = string.ascii_lowercase
doubles = [x + x for x in alphabet]
combs = [''.join(x) for x in zip(alphabet[:-2], alphabet[1:-1], alphabet[2:])] #массив комбинаций
next_letter = {c1: c2 for c1, c2 in zip(alphabet, alphabet[1:]+'a')} #словарь "сдвига" по алфавиту


#функция-проверка строки
def is_valid(st):

    if 'i' in st or 'o' in st or 'l' in st:
        return False

    if sum([x in st for x in doubles]) < 2:
        return False

    if not any([x in st for x in combs]):
        return False

    return True

#создание нового пароля
def next_password(st):
    st = st[:-1] + next_letter[st[-1]]  
    for i in range(-1, -8, -1):
        if st[i] == 'a':
            st = st[:i-1] + next_letter[st[i-1]] + st[i:]
        else:
            break
    return st


with open('input.txt', 'r') as f:
    item = f.readline()

while not is_valid(item):
    item = next_password(item)

item = next_password(item)

while not is_valid(item):
    item = next_password(item)

with open('output2.txt', 'w') as f:
    print(item, file=f)