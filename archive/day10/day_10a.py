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


def strcmd(cmd):
    cmd_str = []
    for word in cmd:
        cmd_str.append(str(word))
    return ' '.join(cmd_str)


test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
cmds_reverse = read_cmds(file_lines)
cmds = cmds_reverse[::-1]

cmd_cycles = {'noop': 1, 'addx': 2}

X = 1
signal_strengths = []
cycle = 1
stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while cmds:
    cmd = cmds.pop()
    op = cmd[0]
    if op == 'addx':
        val = cmd[1]
        stack[1] += val
    num_cycles = cmd_cycles[op]
    for cycle_step in range(num_cycles):
        signal_strength = cycle * X
        signal_strengths.append(signal_strength)
        print(f'cycle {cycle:<5} {strcmd(cmd):10}, signal strength: {signal_strength:<5}, start_X: {X:<3}', end="")
        X += stack[0]
        stack = shift_left(stack)
        print(f', end_X: {X:<3}')
        cycle += 1

sum_signal_strengths = 0
selected_cycles = [20, 60, 100, 140, 180, 220]
selected_cycles_shifted = [idx - 1 for idx in selected_cycles]

for selected_cycle in selected_cycles_shifted:
    sum_signal_strengths += signal_strengths[selected_cycle]
    # print(signal_strengths[selected_cycle])
print()
print(sum_signal_strengths)

print('finished')
# Antwoord: 14040