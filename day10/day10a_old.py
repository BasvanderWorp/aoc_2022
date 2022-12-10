"""
Advent of Code 2022
Day 9

"""
from helpers.io import read_input, split_list
import numpy as np


# numpy array
def read_cmds(lines):
    cmds = []
    for line in lines:
        cmd = line.split()
        if len(cmd) == 2:
            cmd_2 = [cmd[0], int(cmd[1])]
        else:
            cmd_2 = cmd
        cmds.append(cmd_2)
    return cmds


def shift_left(org_list):
    new_list = []
    for idx in range(1, len(org_list)):
        new_list.append(org_list[idx])
    new_list.append(0)
    return new_list

test = False
test = True
input_file = 'input.txt' if not test else 'input_test2.txt'
file_lines = read_input(input_file)
cmds = read_cmds(file_lines)

X = 1
stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for idx, cmd in enumerate(cmds):
    cycle = idx + 1
    if len(cmd) == 2:
        if cmd[0] == 'addx':
            stack[1] += cmd[1]
        X += stack[0]
        stack = shift_left(stack)
        print(f'cycle: {cycle}, X: {X}')
    else:
        print(f'cycle: {cycle}, X: {X}, noop')

# empty stack
while sum(stack) != 0:
    cycle += 1
    X += stack[0]
    stack = shift_left(stack)
    print(f'cycle: {cycle}, X: {X}')


print('finished')
