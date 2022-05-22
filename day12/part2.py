import json

with open('input.txt') as f:
    item = json.load(f)

def sum_of_item(item, skip_red=False):

    if isinstance(item, list):
        return sum([sum_of_item(i, skip_red) for i in item])

    if isinstance(item, dict):
        if skip_red and 'red' in item.values():
            return 0
        return sum([sum_of_item(i, skip_red) for i in item.values()])

    if isinstance(item, str):
        return 0

    if isinstance(item, int):
        return item

with open('output2.txt', 'w') as f:
    print(sum_of_item(item, skip_red=True), file=f)