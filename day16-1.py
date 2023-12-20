# Day 16 - Problem 1

# Using DFS

ground = open('day16-input.txt').read().strip().split('\n')

def energize(start_pos, start_direction):
    queue = [(start_pos, start_direction)]

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

energized = set() # memoizing both position and direction

start_pos = (0, -1) # Start-location of the beam
direction = (0, 1) # Right-wards

energize(start_pos, direction)

tiles = set(tile for tile, dir in energized)
print(len(tiles))