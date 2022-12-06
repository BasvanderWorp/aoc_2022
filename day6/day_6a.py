"""
Advent of Code 2022
Day 6

"""
from helpers.io import read_input, split_list

test = False
test = True
input_file = 'input' if not test else 'input_test'
file_lines = read_input(input_file)
print('asdf')

min_seq = 999999
for line in file_lines:
    remaining = line
    found_idx = 999999
    count = 0
    idx = 4
    found = False
    while len(remaining) > 0 and not found:
        word = remaining[0:4]
        if len(set(word)) == 4:
            found_idx = idx
            found = True
        else:
            remaining = remaining[1:]
            idx = idx + 1
    min_seq = min(min_seq, found_idx)

print(min_seq)
# Test answer : 7
# Answer : 1651