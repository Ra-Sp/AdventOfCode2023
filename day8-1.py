from itertools import cycle

data = list(open('day8-input.txt'))

instruction = cycle(0 if inst == 'L' else 1 for inst in data[0].strip())
mappings = {}

for mapping in data[2:]:
    equal_i = mapping.index('=')
    lhs = mapping[:equal_i-1]
    mappings[lhs] = mapping[equal_i+3:-2].split(', ')

res = 'AAA'

for steps, inst in enumerate(instruction, start=1):
    res = mappings[res][inst]
    if res == 'ZZZ':
        break

print(steps)