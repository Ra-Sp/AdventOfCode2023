# Day 10 - Problem 2

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
steps = 2 # Since we have already considered S and the pipe after S

path_pipes = [node, prev]
path_pipes = {line:[] for line in range(len(ground))}
path_pipes[node[0]].append(node[1])
path_pipes[prev[0]].append(prev[1])

while next(node, prev) != start:
    node, prev = next(node, prev), node
    path_pipes[node[0]].append(node[1])
    steps += 1

nest_area = 0

for x in range(len(ground)):
    in_path = path_pipes[x]
    in_path.sort()
    if in_path:
        for y in range(in_path[0]+1, in_path[-1]):
            if y not in in_path:
                crosses = 0
                # Assuming a ray from ground[x][y] that goes left-wards
                for i in in_path:
                    if i < y:
                        crosses += ground[x][i] in {'J', 'L', '|'}

                if crosses % 2 == 1:
                    nest_area += 1

print(nest_area)


'''
Edge Cases:
F---J and L---7 (any no of '-'s in between)
because there is a chance that the ray might coincide with these borders
'''         


'''
THE RAY CASTING ALGORITHM --
ODD borders crossed => Point is INSIDE the polygon
EVEN borders crossed => Point is OUTSIDE the polygon
'''