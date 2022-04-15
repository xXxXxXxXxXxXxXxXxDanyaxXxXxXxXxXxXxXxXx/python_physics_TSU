matrix = [[0 for x in range(1000)] for y in range(1000)]

with open('input.txt', 'r') as f:
    items = f.readlines()

for item in items:
    if 'on' in item or 'off' in item:
        tmp = item.split()
        instruction, begin, end = tmp[1], tmp[2], tmp[4]
    else:
        tmp = item.split()
        instruction, begin, end = tmp[0], tmp[1], tmp[3]

    x_begin, y_begin = begin.split(",")
    x_end, y_end = end.split(",")

    for x in range(int(x_begin), int(x_end) + 1):
        for y in range(int(y_begin), int(y_end) + 1):

            if instruction == "toggle":
                matrix[x][y] += 2

            if instruction == "on":
                matrix[x][y] += 1

            if instruction == "off" and matrix[x][y] != 0:
                matrix[x][y] -= 1


count = 0
for p in range(1000):
    for q in range(1000):
        count += matrix[p][q]

with open('output2.txt', 'w') as f:
    print(count, file=f)
