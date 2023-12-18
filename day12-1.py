# Day 12 - Problem 1

# The Brute Force Solution -- Takes Significant Time to Compute

from itertools import product

data = open('day12-input.txt')
data = data.read().split('\n')

for i, line in enumerate(data):
    data[i] = line.split()
    data[i][-1] = list(map(int, data[i][-1].split(',')))

def is_valid(pattern, info):
    damaged = []
    damaged_count = 0
    for i in range(len(pattern)):
        if pattern[i] == '#':
            damaged_count += 1
        else:
            if damaged_count != 0:
                damaged.append(damaged_count)
            damaged_count = 0

    if pattern[i] == '#':
        damaged.append(damaged_count)

    return damaged == info


def make_combos(pattern):
    combo_len = pattern.count('?')

    combinations = list(product('#.', repeat=combo_len))
    possible_patterns = []
    for combo in combinations:
        i = 0
        pattern_copy = pattern
        for j, ele in enumerate(pattern_copy):
            if ele == '?':
                pattern_copy = pattern_copy[:j] + combo[i] + pattern_copy[j+1:]
                i += 1
        possible_patterns.append(pattern_copy)
    
    return possible_patterns

valid_arrangements_count = 0

for pattern, info in data:
    arrangements = make_combos(pattern)

    for arrangement in arrangements:
        if is_valid(arrangement, info):
            valid_arrangements_count += 1

print(valid_arrangements_count)
