coordinates = []

with open('input.txt') as f:
    lines = f.read().strip()


coordinates.append([0,0]) #нулевая координата
x, y = 0, 0


for item in lines:
    if item == ">":
        x += 1
    elif item == "^":
        y += 1
    elif item == "<":
        x -= 1
    elif item == "v":
        y -= 1
    if [x,y] not in coordinates:
        coordinates.append([x, y]) #добавляем текущую координату
    else: continue

with open("output1.txt", "w") as f:
    print(len(coordinates), file = f)
