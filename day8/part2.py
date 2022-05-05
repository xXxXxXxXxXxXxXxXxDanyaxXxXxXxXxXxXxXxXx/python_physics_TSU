with open("input.txt") as item:
    N, K = 0, 0
    res = []

    for line in item:
        trim_line = line[:-1]
        escaped_quotes = trim_line.replace("\\", "\\\\")
        escaped_slashes = escaped_quotes.replace("\"", "\\\"")
        N += len(trim_line)
        K += (len(escaped_slashes) + 2)
        res.append(trim_line)


with open('output2.txt', 'w') as f:
    print(str(K - N), file=f)
