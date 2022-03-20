floor = 0

with open("input.txt") as f:
    st = ''.join(f.readlines())

for i in st:
    if i == "(":
        floor += 1
    else:
        floor -= 1

print(floor)