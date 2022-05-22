with open('input.txt', 'r') as f:
    items = f.read()
    
totalsec = 2503
best = 0

for item in items.split('\n'):
    n, _, _, speed, _, _, ftime,  _, _, _, _, _, _, rtime, _ = item.split(" ")
    speed, ftime, rtime = int(speed), int(ftime), int(rtime)
    dist = 0

    cycle = ftime + rtime
    bursts = totalsec // cycle
    dist += speed * ftime * bursts

    leftover = totalsec % cycle
    dist += speed * min(leftover, ftime)

    if dist > best: best = dist

with open('output1.txt', 'w') as f:
    print(best, file=f)