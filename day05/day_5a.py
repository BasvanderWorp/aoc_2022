"""
Advent of Code 2022
Day 5

https://adventofcode.com/2022/day/5/input
"""
def read_crates(input_file='input', remove_newlines=True, split_on_comma=False, split_on_space=False,
               dtype='string', sublists_on_newline=False):
    with open(input_file, 'r') as f:
        file_lines = f.readlines()
    file_lines_part_1 = []
    for _, file_line in enumerate(file_lines):
        if file_line != '\n':
            file_lines_part_1.append(file_line)
    crates = []
    for line in file_lines_part_1:
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

def read_moves(input_file='input', remove_newlines=True, split_on_comma=False, split_on_space=False,
               dtype='string', sublists_on_newline=False):
    with open(input_file, 'r') as f:
        file_lines = f.readlines()
    file_lines_part_1 = []
    moves = []
    for _, file_line in enumerate(file_lines):
        if file_line[0:4] == 'move':
            number_to_move = int(file_line.split('move ')[1].split(' from ')[0])
            from_crate = int(file_line.split(' from ')[1].split(' to ')[0])
            to_crate = int(file_line.split(' to ')[1][:-1])
            moves.append([number_to_move, from_crate, to_crate])
    return moves

test = False
# test = True
input_file = 'input' if not test else 'input_test'
crates = read_crates(input_file)
moves = read_moves(input_file)

# crates = [['N', 'Z'], [['D', 'C', 'M'], ['P']]

for move in moves:
    for crate_num in range(move[0]):
        crate_to_move = crates[move[1]-1][0]
        del(crates[move[1]-1][0])
        crates[move[2]-1].insert(0, crate_to_move)


print(''.join([crate[0] for crate in crates]))
print('finished')