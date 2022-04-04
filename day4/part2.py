import hashlib

with open('input.txt','r', encoding='utf-8') as f:
    origin = f.readline()

i = 0
while True:
    key = origin + str(i)
    res = hashlib.md5(key.encode())
    hexdigit = str(res.hexdigest())

    if not ('000000' in ''.join(hexdigit[0:6].split())):
        i += 1
    else:
        break

with open("output2.txt", "w") as f:
    print(i, file = f)