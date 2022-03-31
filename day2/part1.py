paper_summ = 0

with open("input.txt") as f:
    for i in f.readlines():
        l, w, h = list(map(int, list(i.split('x'))))
        s1, s2, s3 = l * w, w * h, l * h
        extra = min(s1, s2, s3)
        summ = (2 * s1 + 2 * s2 + 2 * s3) + extra
        paper_summ += summ


with open("output1.txt", "w") as f:
    print(paper_summ, file=f)
