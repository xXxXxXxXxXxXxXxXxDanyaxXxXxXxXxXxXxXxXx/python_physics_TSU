with open("input.txt") as f:
    item = f.read().split('\n')

def count_char(s):
    return len(s) + 2 + len(list(filter(lambda x: x in '\\"', s)))

total = 0
for line in item:
    total += count_char(line) - len(line)

with open('output2.txt', 'w') as f:
    print(total, file=f)