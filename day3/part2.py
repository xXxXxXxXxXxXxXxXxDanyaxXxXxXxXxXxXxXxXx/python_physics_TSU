coordinates = []

with open('input.txt') as f:
    lines = f.read().strip()

santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
turn = 0 #очередь санта-робот

for item in lines:
    if turn == 0: #очередь санты
        if item == ">":
            santa_x += 1
        elif item == "^":
            santa_y += 1
        elif item == "<":
            santa_x -= 1
        elif item == "v":
            santa_y -= 1

        turn = 1 #меняем очередь на робота
        if [santa_x, santa_y] not in coordinates:
            coordinates.append([santa_x, santa_y])

    elif turn == 1:
        if item == ">":
            robo_x += 1
        elif item == "^":
            robo_y += 1
        elif item == "<":
            robo_x -= 1
        elif item == "v":
            robo_y -= 1

        turn = 0
    if [robo_x, robo_y] not in coordinates:
            coordinates.append([robo_x, robo_y])


with open("output2.txt", "w") as f:
    print(len(coordinates), file = f)
