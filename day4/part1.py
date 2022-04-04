import hashlib

with open('input.txt','r', encoding='utf-8') as f:
    origin = f.readline()

i = 0
while True:
    key = origin + str(i)
    res = hashlib.md5(key.encode())
    hexdigit = str(res.hexdigest())

    if not ('00000' in ''.join(hexdigit[0:5].split())):
        i += 1
    else:
        break

with open("output1.txt", "w") as f:
    print(i, file = f)