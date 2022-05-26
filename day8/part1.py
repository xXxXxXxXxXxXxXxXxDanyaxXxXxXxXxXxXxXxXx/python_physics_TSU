with open("input.txt") as f:
    item = f.read().split('\n')

def count_char(s):
    s = s[1:-1]
    count = 0
    i = 0
    while i < len(s):
        count += 1
        if s[i] == '\\':
            if s[i+1] == 'x':
                i += 4
            else:
                i += 2
        else:
            i += 1
    return count

total =  0

for line in item:
    total += len(line) - count_char(line)

with open('output1.txt', 'w') as f:
    print(total, file=f)
