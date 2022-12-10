"""
Advent of Code 2022
Day 5

https://adventofcode.com/2022/day/5/input
"""
from helpers.io import read_input, split_list


def read_crates(lines):
    crates = []
    for line in lines:
        for idx, char in enumerate(line):
            if char not in [' ', '[', ']', '\n'] and char.isupper():
                # 1, 5, 9
                crate_num = (idx - 1) // 4 + 1
                if len(crates) < crate_num:
                    for idx_new in range(len(crates), crate_num):
                        crates.append([])
                    crates[crate_num - 1].append(char)
                else:
                    crates[crate_num - 1].append(char)
    return crates


def read_moves(lines):
    moves = []
    for file_line in lines:
        if file_line[0:4] == 'move':
            number_to_move = int(file_line.split('move ')[1].split(' from ')[0])
            from_crate = int(file_line.split(' from ')[1].split(' to ')[0])
            to_crate = int(file_line.split(' to ')[1])
            moves.append([number_to_move, from_crate, to_crate])
    return moves


test = False
test = True
input_file = 'input' if not test else 'input_test'
# Read crates in data structure, which data structure would be best?
#   crates = [['N', 'Z'], [['D', 'C', 'M'], ['P']]
#   or a stack like structure, does python have a stack? push and pop.
#   you can do push and pop with a list can't you?

file_lines = read_input(input_file)
lists = split_list(file_lines, r"")
crates = read_crates(lists[0])
moves = read_moves(lists[1])


for move in moves:
    for crate_num in range(move[0]):
        crate_to_move = crates[move[1]-1][0]
        del(crates[move[1]-1][0])
        crates[move[2]-1].insert(0, crate_to_move)


print(''.join([crate[0] for crate in crates]))
print('finished')