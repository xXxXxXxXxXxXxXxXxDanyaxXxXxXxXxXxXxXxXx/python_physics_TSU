from re import sub


def statement(velocity, moving_time, stop_time):
    time = 2503
    distance = 0
    counter = 0
    state = 0
    while counter < time:
        if state == 0:
            if counter + moving_time < time:
                distance += velocity * moving_time
            else:
                distance += velocity * (time - counter)
            counter += moving_time
            state = 1
        elif state == 1:
            counter += stop_time
            state = 0
    return distance


array = []
with open('input.txt', 'r') as f:
    for line in f:
        line = sub(r'can fly | km/s for| (seconds, but then must rest for)| seconds.', '', line)
        array.append(line.split())

res = []
for element in array:
    obj = statement(int(element[1]), int(element[2]), int(element[3]))
    res.append(obj)

with open('output1.txt', 'w') as f:
    print(str(max(res)), file=f)
