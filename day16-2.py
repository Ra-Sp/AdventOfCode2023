# Day 16 - Problem 2

ground = open('day16-input.txt').read().strip().split('\n')

def energize(start_pos, start_direction):
    queue = [(start_pos, start_direction)]
    energized = set()

    while queue:

        curr_pos, curr_direction = queue.pop(0)
        beam = curr_pos[0] + curr_direction[0], curr_pos[1] + curr_direction[1]
        
        if not (0 <= beam[0] < len(ground) and 0 <= beam[1] < len(ground[0])) or (beam, curr_direction) in energized:
            continue

        if ground[beam[0]][beam[1]] == '.':
            energized.add((beam, curr_direction))
            queue.append((beam, curr_direction))
        
        elif ground[beam[0]][beam[1]] == '|':
            energized.add((beam, curr_direction))
            
            if curr_direction == (0, 1) or curr_direction == (0, -1):
                queue.append((beam, (1, 0))) # Down
                queue.append((beam, (-1, 0))) # Up
            
            else:
                queue.append((beam, curr_direction)) # Cotinue in the same direction
        
        elif ground[beam[0]][beam[1]] == '-':
            energized.add((beam, curr_direction))
            
            if curr_direction == (1, 0) or curr_direction == (-1, 0):
                queue.append((beam, (0, 1))) # Right
                queue.append((beam, (0, -1))) # Left
            
            else:
                queue.append((beam, curr_direction)) # Cotinue in the same direction
        
        elif ground[beam[0]][beam[1]] == '\\':
            energized.add((beam, curr_direction))
            direction = curr_direction[::-1]
            queue.append((beam, direction))
        
        elif ground[beam[0]][beam[1]] == '/':
            energized.add((beam, curr_direction))
            direction = curr_direction[::-1]
            direction = direction[0] * -1, direction[1] * -1
            queue.append((beam, direction))   

    return  count_energized_tiles(energized)

def count_energized_tiles(energized):
    tiles = set(tile for tile, dir in energized)
    return len(tiles)

energized_tiles_count = []
energized = set()

rows = len(ground)
cols = len(ground[0])

# Energizing from the Top Edge
start_direction = (1, 0)
for col in range(cols):
    start_pos = (-1, col)
    energized_tiles_count.append(energize(start_pos, start_direction))

# Energizing from the Bottom Edge
start_direction = (-1, 0)
for col in range(cols):
    start_pos = (rows, col)
    energized_tiles_count.append(energize(start_pos, start_direction))

# Energizing from the Left Edge
start_direction = (0, 1)
for row in range(rows):
    start_pos = (row, -1)
    energized_tiles_count.append(energize(start_pos, start_direction))

# Energizing from the Right Edge
start_direction = (0, -1)
for row in range(rows):
    start_pos = (row, cols)
    energized_tiles_count.append(energize(start_pos, start_direction))

print(max(energized_tiles_count))