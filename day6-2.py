# Day 6 - Problem 2

data = list(open('day6-input.txt'))
time = list(data[0][5:].lstrip().rstrip().split())
dist = list(data[1][9:].lstrip().rstrip().split())
T = ""
D = ""

for digit in time:
    if digit:
        T += digit

for digit in dist:
    if digit:
        D += digit

T = int(T)
D = int(D)

all_ways = 0
for t in range(T // 2 + 1):
    dist_covered = (T - t) * t
    if dist_covered > D:
        all_ways += 1
all_ways *= 2
if T % 2 == 0:
    all_ways -= 1

print(all_ways)
