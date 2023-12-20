# Day 15 - Problem 1

intialization_seq = open('day15-input.txt').read().strip().split(',')

curr_val = 0

def hash(seq):
    seq_val = 0
    for ch in seq:
        seq_val += ord(ch)
        seq_val *= 17
        seq_val %= 256
    return seq_val

for seq in intialization_seq:
    curr_val += hash(seq)

print(curr_val)