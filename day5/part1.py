with open('input.txt','r', encoding='utf-8') as f:
    st = f.readlines()


def is_good(st):
    for s in ['ab', 'cd', 'pq', 'xy']: 
        if s in st: return False
    vowels = (st.count('a') + st.count('e') + st.count('i') + st.count('o') + st.count('u'))

    if vowels < 3: return False

    if any([st[i] == st[i+1] for i in range(len(st) - 1)]):
        return True
    else:
        return False

i = 0
for line in st:
    if is_good(line):
        i += 1
print(i)

