# Day 11 - Problem 1

''' Check day11-2.py for a generalised approach '''

from itertools import combinations

obs = open('day11-input.txt') # The observations
obs = obs.read().split('\n')
obs_copy = obs.copy()
galaxies = []


def expand_universe():
    global obs
    row = 0
    while row < len(obs):
        if set(obs[row]) == {'.'}:
            obs.insert(row, obs[row])
            row += 1
        row += 1

# Checking for galaxy-less rows and expanding
expand_universe()

# Transposing obs
obs = [[obs[row][col] for row in range(len(obs))] for col in range(len(obs[0]))]

# Checking for galaxy-less cols (in the original obs) and expanding
expand_universe()

# Re-transposing obs
max_row_length = max(len(row) for row in obs)
obs = [[obs[row][col] for row in range(len(obs))] for col in range(len(obs[0]))]

# Locating the galaxies '#'
for row, line in enumerate(obs):
    for col, obj in enumerate(line):
        if obj == '#':
            galaxies.append((row, col))

galaxy_combos = list(combinations(galaxies, 2))

shortest_paths_sum = 0
for galaxy1, galaxy2 in galaxy_combos:
    shortest_paths_sum += (abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]))

print(shortest_paths_sum)