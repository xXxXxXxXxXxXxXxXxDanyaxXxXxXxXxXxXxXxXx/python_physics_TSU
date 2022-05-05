import re
a = "P"
with open("input.txt") as item:
    N, K = 0, 0
    res = []
    for line in item:
        trim_line = line[:-1]
        no_line = trim_line.replace("\\\\", a)
        no_quotes = no_line.replace("\\\"", a)
        no_hexcode_line = re.sub("\\\\x..", a, no_quotes)

        N += len(trim_line)
        K += (len(no_hexcode_line) - 2)
        res.append(trim_line)

with open('output1.txt', 'w') as f:
    print(str(N - K), file=f)

