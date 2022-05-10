with open("input.txt", "r") as f:
    item = f.readline()


for elem in item:
    if not(elem.isdigit()) and elem != "-":
        item = item.replace(elem, '.')


arr, res = item.split('.'), []
for elem in arr:
    if elem != "":
        res.append(int(elem))

with open('output1.txt', 'w') as f:
    print(int(sum(res)), file=f)
