# Day 14 - Problem 2

data = open('day14-input.txt').read().strip().split('\n')

platform = []
for line in data:
    platform.append(list(line))

def transpose(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed

def tilt_left(platform):
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

def reverse_rows(platform):
    return [row[::-1] for row in platform]

def calculate_load(platform):
    load = 0
    for i, row in enumerate(platform):
        load += (len(platform) - i) * row.count('O')
    return load

states_record = []

tilt_count = 0
platform = platform

for spin_count in range(1000000000):

    # Tilt North
    platform = transpose(tilt_left(transpose(platform)))
    tilt_count += 1

    # Tilt West
    platform = tilt_left(platform)
    tilt_count += 1

    # Tilt South
    platform = transpose(reverse_rows(tilt_left(reverse_rows(transpose(platform)))))
    tilt_count += 1
    
    # Tilt East
    platform = reverse_rows(tilt_left(reverse_rows(platform)))
    tilt_count += 1

    if platform in states_record:
        repeat_start = states_record.index(platform)
        period = spin_count - repeat_start
        platform = states_record[(10**9 - 1 - repeat_start) % period + repeat_start]  
        break
    
    states_record.append(platform)

tot_load = calculate_load(platform)
print(tot_load)


'''
North Tilt -- Transpose, Tilt left, Transpose Again
West Tilt -- Tilt left
South Tilt -- Transpose, Reverse rows, Tilt left, Reverse rows again, Transpose Again
East Tilt -- Reverse rows, Tilt left, Reverse rows again
'''

