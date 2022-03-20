floor = 0

with open("input.txt") as f:
	st = ''.join(f.readlines())

for i in range(len(st)):
	if floor >= 0:
		if st[i] == "(":
			floor += 1
		else:
			floor -= 1
	else:
		print(i)
		break
		
print(floor)
