with open('input.txt','r', encoding='utf-8') as f:
    st = f.readlines()

def is_good(st):

    if not any([st[i] == st[i+2] for i in range(len(st)-2)]):
        return False
    if any([(st.count(st[i:i+2])>=2) for i in range(len(st)-2)]):
        return True

    return False


i = 0
for line in st:
    if is_good(line):
        i += 1


with open("output2.txt", "w") as f:
    print(i, file = f)
