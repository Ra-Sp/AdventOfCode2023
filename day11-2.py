# Day 11 - Problem 2

from itertools import combinations

obs = open('day11-input.txt') # The observations
obs = obs.read().split('\n')
obs_copy = obs.copy()
galaxies = []
empty_rows, empty_cols = [], []

# The '1' is subtracted to count the already present empty row/col

'''For Problem 1'''
expansion_multiplier = 2 - 1

'''For Problem 2'''
expansion_multiplier = 1000000 - 1

# Locating the galaxies '#'
for row, line in enumerate(obs):
    for col, obj in enumerate(line):
        if obj == '#':
            galaxies.append([row, col])

# Finding empty rows
for i, row in enumerate(obs):
    if set(row) == {'.'}:
        empty_rows.append(i)

# Transposing obs
obs = [[obs[row][col] for row in range(len(obs))] for col in range(len(obs[0]))]

# Finding empty rows
for i, row in enumerate(obs):
    if set(row) == {'.'}:
        empty_cols.append(i)

# On expanding the Universe
for i, galaxy in enumerate(galaxies):
    updated_row, updated_col = galaxy[0], galaxy[1]
    for row in empty_rows:
        if row > galaxy[0]:
            break
        updated_row += expansion_multiplier
    for col in empty_cols:
        if col > galaxy[1]:
            break
        updated_col += expansion_multiplier
    galaxies[i] = [updated_row, updated_col]

galaxy_combos = list(combinations(galaxies, 2))

shortest_paths_sum = 0
for galaxy1, galaxy2 in galaxy_combos:
    shortest_paths_sum += (abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]))

print(shortest_paths_sum)
