# Day 13 - Problem 1

patterns = open('day13-input.txt')
patterns = list(patterns.read().split('\n\n'))

summary = 0

for pattern in patterns:
    mirror_row, mirror_col = 0, 0
    pattern = pattern.strip().split('\n')
    
    # To get the mirror row
    mirror = len(pattern) - 1
    while mirror >= 0:
        smaller_part = min(mirror, len(pattern) - mirror)
        if pattern[mirror:mirror+smaller_part][::-1] == pattern[mirror-smaller_part:mirror]:
            mirror_row = mirror
            break
        mirror -= 1
    
    # To get the mirror col
    pattern = list(zip(*pattern))  # Transposing the pattern
    mirror = len(pattern) - 1
    while mirror >= 0:
        smaller_part = min(mirror, len(pattern) - mirror)
        if pattern[mirror:mirror+smaller_part][::-1] == pattern[mirror-smaller_part:mirror]:
            mirror_col = mirror
            break
        mirror -= 1

    summary += (mirror_row * 100) + mirror_col

print(summary)