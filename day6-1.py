data = list(open('day6-input.txt'))
time = list(map(int, data[0][5:].lstrip().rstrip().split()))
dist = list(map(int, data[1][9:].lstrip().rstrip().split()))

results = []
i = 0
for T in time:
    all_ways = 0
    for t in range(T // 2 + 1):
        dist_covered = (T - t) * t
        if dist_covered > dist[i]:
            all_ways += 1
    all_ways *= 2
    if T % 2 == 0:
        all_ways -= 1
    results.append(all_ways)
    i += 1

prod = 1
ans = [prod := prod * ways for ways in results]

print(prod)