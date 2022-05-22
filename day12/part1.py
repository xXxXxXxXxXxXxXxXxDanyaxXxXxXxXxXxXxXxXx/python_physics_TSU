import re

with open("input.txt", "r") as f:
    item = f.read()

with open('output1.txt', 'w') as f:
    print((sum(int(x) for x in re.findall('-?[0-9]+', item))), file=f)

