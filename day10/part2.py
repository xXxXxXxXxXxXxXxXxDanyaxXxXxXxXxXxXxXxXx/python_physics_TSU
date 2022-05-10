def look_and_say(n):
    i = 0
    res = []
    while i < len(n):
        count = 1
        while i+1 < len(n) and n[i] == n[i+1]:
            count += 1
            i += 1
        res.append(str(count) + n[i])
        i += 1

    return (''.join(res))


with open('input.txt', 'r') as f:
    item = f.readline()

for _ in range(50):
    item = look_and_say(item)

with open('output2.txt', 'w') as f:
    print(len(str(item)), file=f)
