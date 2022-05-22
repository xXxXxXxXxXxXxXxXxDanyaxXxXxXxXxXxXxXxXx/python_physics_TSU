import json

with open("input.txt", "r") as f:
    item = f.read()


def func(obj):

    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        else:
            return func(obj.values())

    if isinstance(obj, list):
        return sum(func(x) for x in obj)

    if isinstance(obj, int):
        return obj

    return 0


with open('output2.txt', 'w') as f:
    print(func(json.loads(item)), file=f)
