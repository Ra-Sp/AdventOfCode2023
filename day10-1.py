# Day 10 - Problem 1

from math import ceil

data = list(open('day10-input.txt'))
ground = []
for line in data:
    ground.append(line.strip())
    if 'S' in line:
        start = (ground.index(line.strip()), line.index('S'))

def next(node, prev):
    if ground[node[0]][node[1]] == '|':
        if prev[0] == node[0] - 1:
            return (node[0]+1, node[1])
        else:
            return (node[0]-1, node[1])
    elif ground[node[0]][node[1]] == '-':
        if prev[1] == node[1] - 1:
            return (node[0], node[1]+1)
        else:
            return (node[0], node[1]-1)
    elif ground[node[0]][node[1]] == 'L':
        if prev[0] == node[0] - 1:
            return (node[0], node[1]+1)
        else:
            return (node[0]-1, node[1])
    elif ground[node[0]][node[1]] == 'J':
        if prev[0] == node[0] - 1:
            return (node[0], node[1]-1)
        else:
            return (node[0]-1, node[1])
    elif ground[node[0]][node[1]] == '7':
        if prev[0] == node[0] + 1:
            return (node[0], node[1]-1)
        else:
            return (node[0]+1, node[1])
    elif ground[node[0]][node[1]] == 'F':
        if prev[0] == node[0] + 1:
            return (node[0], node[1]+1)
        else:
            return (node[0]+1, node[1])
    else:
        return
    

node, prev = (start[0]+1, start[1]), start # Found the pipe after S from the input data
steps = 2 # Since we have already considered S and the pipe next to S

while next(node, prev) != start:
    node, prev = next(node, prev), node
    steps += 1

print(ceil(steps/2)) # The farthest point from S is also the mid-point of the loop