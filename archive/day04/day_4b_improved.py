"""
Advent of Code 2022
Day 4
"""


def read_input(input_file='input', remove_newlines=True, split_on_comma=False, split_on_space=False):
    with open(input_file, 'r') as f:
        file_lines = f.readlines()
    if remove_newlines:
        # remove new lines
        file_lines = [line.split('\n')[0] for line in file_lines]
    if split_on_comma:
        file_lines = [line.split(',') for line in file_lines]
    if split_on_space:
        file_lines = [line.split(' ') for line in file_lines]
    return file_lines


def convert_ranges_to_sets(list_of_range_pairs):
    set_pairs = []
    for range_pair in list_of_range_pairs:
        set_pair = []
        for hyphen_range in range_pair:
            spaces_list = []
            for x in range(int(hyphen_range.split('-')[0]), int(hyphen_range.split('-')[1]) + 1):
                spaces_list.append(x)
            set_pair.append(set(spaces_list))
        set_pairs.append(set_pair)
    return set_pairs

file_lines = read_input('input', split_on_comma=True)
set_pairs = convert_ranges_to_sets(file_lines)
overlapping_pairs_count = 0
for pair in set_pairs:
    if pair[0] & pair[1]:
        overlapping_pairs_count += 1

print(overlapping_pairs_count)

