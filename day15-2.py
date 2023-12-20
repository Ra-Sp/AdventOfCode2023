# Day 15 - Problem 2

intialization_seq = open('day15-input.txt').read().strip().split(',')

boxes = {}

def hash(seq):
    seq_val = 0
    for ch in seq:
        seq_val += ord(ch)
        seq_val *= 17
        seq_val %= 256
    return seq_val

def add_lens(seq):
    symbol_i = seq.index('=')
    label = seq[:symbol_i]
    focal_len = seq[symbol_i+1:]
    box = hash(label)
    
    if box not in boxes:
        boxes[box] = [[label, focal_len]] # Adding the lens to an empty box
    else:
        for lens in boxes[box]:
            if lens[0] == label:
                lens[-1] = focal_len # Replacing the lens
                return
            
        boxes[box].append([label, focal_len]) # Adding to the front of the box
        
def remove_lens(seq):
    label = seq[:-1]
    box = hash(label)
    if box in boxes:
        for lens in boxes[box]:
            if lens[0] == label:
                boxes[box].remove(lens)
                return
        
def calculate_foc_power(boxes):
    tot_power = 0
    for box in boxes:
        power = 0
        for i, lens in enumerate(boxes[box]):
            power += (box+1) * (i+1) * int(lens[-1])
        tot_power += power
    
    return tot_power


for seq in intialization_seq:
    if '=' in seq:
        add_lens(seq)
    else:
        remove_lens(seq)

result_focusing_power = calculate_foc_power(boxes)
print(result_focusing_power)