# Day 14 - Problem 1

platform = open('day14-input.txt')

platform  = platform.read().strip().split('\n')

def transpose(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed

def tilt_platform(platform):
    for row in platform:
        rounds = 0
        cube = -1
        spaces = []
        i = 0
        while rounds != row.count('O'):
            rock = row[i]
            if rock == 'O':
                if spaces and (cube == -1 or cube < spaces[0]):
                        row[spaces.pop(0)] = rock
                        row[i] = '.'
                        rounds += 1
                        continue
                rounds += 1
            elif rock == '#':
                cube = i
                spaces = []
            else:
                spaces.append(i)
            i += 1

    return platform

def calculate_load(platform):
    load = 0
    for i, row in enumerate(platform):
        load += (len(platform) - i) * row.count('O')
    return load

platform = transpose(platform)
tilted_platform = transpose(tilt_platform(platform))

tot_load = calculate_load(tilted_platform)
print(tot_load)



