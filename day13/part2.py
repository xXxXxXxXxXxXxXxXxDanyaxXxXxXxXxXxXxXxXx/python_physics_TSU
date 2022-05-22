import itertools, math

pairs = dict()
names = set()

with open('input.txt', 'r') as f:
    item = f.read()


for st in item.split('\n'):
    a, _, dr, sz, _, _, _, _, _, _, b = st[:-1].split(' ')
    names.add(b)
    pairs[(a, b)] = int(sz) * (1 if dr == 'gain' else -1)

names.add('me')
for x in names: pairs[(x, 'me')] =  pairs[('me', x)] = 0
best = -math.inf

for arr in itertools.permutations(list(names)):
    cost = pairs[(arr[0], arr[-1])] + pairs[(arr[-1], arr[0])]
    for a, b in zip(arr[:-1], arr[1:]):
        cost += pairs[(a, b)] + pairs[(b, a)]

    if cost > best:
        best = cost

with open('output2.txt', 'w') as f:
    print(best, file=f)