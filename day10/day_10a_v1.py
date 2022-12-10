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
test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
cmds = read_cmds(file_lines)

cmd_cycles = {'addx': 2}

X = 1
signal_strengths = []
stack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cycle = 1
for idx, cmd in enumerate(cmds):
    signal_strength = cycle * X
    signal_strengths.append(signal_strength)
    print(f'cycle: {cycle}, cmd: {strcmd(cmd)}, ss: {signal_strength}, start_X: {X}', end="")
    if len(cmd) == 2:
        if cmd[0] == 'addx':
            stack[1] += cmd[1]
            for cycle_step in range(cmd_cycles[cmd[0]]):
                if cycle_step > 0:
                    signal_strength = cycle * X
                    signal_strengths.append(signal_strength)
                    print(f'cycle: {cycle}, cmd: {strcmd(cmd)}, ss: {signal_strength}, start_X: {X}', end="")
                X += stack[0]
                stack = shift_left(stack)
                print(f', end_X: {X}')
                cycle += 1
    else:
        print(f', end_X: {X}, noop')
        cycle += 1

# empty stack
while sum(stack) != 0:
    cycle += 1
    X += stack[0]
    stack = shift_left(stack)
    print(f'cycle: {cycle}, X: {X}')

sum_signal_strengths = 0
selected_cycles = [20, 60, 100, 140, 180, 220]
selected_cycles_shifted = [idx - 1 for idx in selected_cycles]

for selected_cycle in selected_cycles_shifted:
    sum_signal_strengths += signal_strengths[selected_cycle]
    print(signal_strengths[selected_cycle])
print(sum_signal_strengths)

print('finished')
