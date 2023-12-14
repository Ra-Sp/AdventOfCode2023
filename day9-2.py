data = list(open('day9-input.txt'))
first_vals_sum = 0

for line in data:
    history = list(map(int, line.strip().split()))
    first_vals = history[0]
    subtract = True
    while set(history) != {0}:
        history = [history[i] - history[i-1] for i in range(1, len(history))]

        if subtract:
            first_vals -= history[0]
        else:
            first_vals += history[0]
        subtract = not subtract

    first_vals_sum += first_vals

print(first_vals_sum)