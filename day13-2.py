# Day 13 - Problem 2

patterns = open('day13-input.txt')
patterns = list(patterns.read().split('\n\n'))

summary = 0

def transpose(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        transposed.append(''.join(row))
    return transposed

def differences_in_lines(line1, line2):
    differences = 0
    for i, symbol in enumerate(line1):
        if line2[i] != symbol:
            differences += 1
    return differences

def restore(pattern):
    # Checking row-wise

    mirror = 0
    while mirror < len(pattern) - 1:
        smudges = 0
        corrector = None
        smaller_part = min(mirror + 1, len(pattern) - mirror - 1)

        for i in range(smaller_part):
            if pattern[mirror-i] != pattern[mirror+1+i]:
                smudges += differences_in_lines(pattern[mirror-i], pattern[mirror+1+i])
                if smudges == 1 and not corrector:
                    corrector = i
                
        if smudges == 1:
            pattern[mirror+1+corrector] = pattern[mirror-corrector] # Removing the smudge
            return pattern
        mirror += 1
        
    # Checkign col-wise
        
    pattern = transpose(pattern)  # Transposing the pattern
    
    mirror = 0
    while mirror < len(pattern) - 1:
        smudges = 0
        corrector = None
        smaller_part = min(mirror + 1, len(pattern) - mirror - 1)

        for i in range(smaller_part):
            if pattern[mirror-i] != pattern[mirror+1+i]:
                smudges += differences_in_lines(pattern[mirror-i], pattern[mirror+1+i])
                if smudges == 1 and not corrector:
                    corrector = i
                
        if smudges == 1:
            pattern[mirror+1+corrector] = pattern[mirror-corrector] # Removing the smudge
            pattern = transpose(pattern)  # Re-transposing the pattern
            return pattern
        mirror += 1
    
    pattern = transpose(pattern)  # Re-transposing the pattern
    return pattern

def find_reflection_line(pattern):
    mirror_rows, mirror_cols = [], []
    
    # To get the mirror row

    mirror = 0
    while mirror < len(pattern) - 1:
        smaller_part = min(mirror + 1, len(pattern) - mirror - 1)
        if pattern[mirror+1:mirror+1+smaller_part][::-1] == pattern[mirror-smaller_part+1:mirror+1]:
            mirror_rows.append(mirror)
        mirror += 1
    
    # To get the mirror col
        
    pattern = transpose(pattern)  # Transposing the pattern
    
    mirror = 0
    while mirror < len(pattern) - 1:
        smaller_part = min(mirror + 1, len(pattern) - mirror - 1)
        if pattern[mirror+1:mirror+1+smaller_part][::-1] == pattern[mirror-smaller_part+1:mirror+1]:
            mirror_cols.append(mirror)
        mirror += 1

    return mirror_rows, mirror_cols


for i, pattern in enumerate(patterns):
    pattern = pattern.strip().split('\n')

    prev_mirror_rows, prev_mirror_cols = find_reflection_line(pattern)

    # The same pattern is returned if there isn't any smudge
    restored_pattern = restore(pattern)

    mirror_rows, mirror_cols = find_reflection_line(restored_pattern)

    if not mirror_rows or (prev_mirror_rows and prev_mirror_rows == mirror_rows):
        mirror_row = 0
    
    else:
        if not prev_mirror_rows:
            mirror_row = max(mirror_rows) + 1
        else:
            mirror_row = max(set(mirror_rows) - set(prev_mirror_rows)) + 1

    if not mirror_cols or (prev_mirror_cols and prev_mirror_cols == mirror_cols):
        mirror_col = 0
    
    else:
        if not prev_mirror_cols:
            mirror_col = max(mirror_cols) + 1
        else:
            mirror_col = max(set(mirror_cols) - set(prev_mirror_cols)) + 1
    
    # print(i, ((mirror_row) * 100) + (mirror_col))

    summary += ((mirror_row) * 100) + (mirror_col)

print(summary)