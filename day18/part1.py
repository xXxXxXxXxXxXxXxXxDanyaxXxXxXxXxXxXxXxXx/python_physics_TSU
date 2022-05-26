with open('input.txt', 'r') as f:
    item = f.read()


item = [[1 if x == "#" else 0 for x in line] for line in item.split('\n')]
vol = len(item)


def switch(curr):
    def get_neighbor(row, col):
        if 0 <= row < vol and 0 <= col < vol:
            return curr[row][col]
        else:
            return 0

    def count_neighbor(row, col):
        sum = -curr[row][col]
        for i in range(-1, 2):
            for j in range(-1, 2):
                sum += get_neighbor(row + i, col + j)
        return sum

    def rule(row, col):
        state, neighbor = curr[row][col], count_neighbor(row, col)
        if state == 1 and neighbor in (2, 3):
            return 1
        elif state == 0 and neighbor == 3:
            return 1
        return 0
    return [[rule(row, col) for col in range(vol)] for row in range(vol)]


for i in range(100):
    item = switch(item)

with open('output1.txt', 'w') as f:
    print(sum(sum(row) for row in item), file=f)
