# Day 8 - Problem 2

from itertools import cycle
from math import lcm

data = list(open('day8-input.txt'))

instruction = cycle(0 if inst == 'L' else 1 for inst in data[0].strip())
mappings = {}

nodes = []

for mapping in data[2:]:
    equal_i = mapping.index('=')
    lhs = mapping[:equal_i-1]
    mappings[lhs] = mapping[equal_i+3:-2].split(', ')
    if lhs[-1] == 'A':
        nodes.append(lhs)

cycles = []
for node in nodes:
    for steps, inst in enumerate(instruction, start=1):
        node = mappings[node][inst]
        if node[-1] == 'Z':
            cycles.append(steps)
            break
        
print(lcm(*cycles))
