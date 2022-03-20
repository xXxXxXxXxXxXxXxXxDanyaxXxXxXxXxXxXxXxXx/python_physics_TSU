ribbon_summ = 0

with open("input.txt") as f:
	for i in f.readlines():
		l, w, h = list(map(int, list(i.split('x'))))
		rib = min(2*l+2*h, 2*w+2*h, 2*l+2*w)
		bow = l*w*h
		ribbon_summ += (rib + bow)

print(ribbon_summ)