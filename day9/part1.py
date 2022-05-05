import re, itertools

def calc(f):
    locations = set()
    distance = {}

    for line in f:
        start, end = line.split(" ")[0], line.split(" ")[2]

        locations.add(start)
        locations.add(end)

        distance_between = int(re.findall("\d+", line)[0])
        distance[(start, end)] = distance_between
        distance[(end, start)] = distance_between

    return locations, distance


with open("input.txt") as f1:
    (locations, distance) = calc(f1)

    path_lengths = {}

    for path in itertools.permutations(locations):
        segments = [(path[i], path[i + 1]) for i in range(0, len(locations) - 1)]
        lengths = [distance[segment] for segment in segments]

        path_lengths[path] = sum(lengths)

with open('output1.txt', 'w') as f2:
    print(str(min(path_lengths.values())), file=f2)