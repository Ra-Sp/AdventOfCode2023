# Day 9 - Problem 1

data = list(open('day9-input.txt'))
next_val_sum = 0

for line in data:
    history = list(map(int, line.strip().split()))
    next_val = history[-1]
    while set(history) != {0}:
        history = [history[i] - history[i-1] for i in range(1, len(history))]
        next_val += history[-1]
    next_val_sum += next_val

print(next_val_sum)
