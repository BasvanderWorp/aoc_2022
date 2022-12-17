"""
Advent of Code 2022
Day 9

"""
from helpers.io import read_input, split_list
import numpy as np



def strcmd(cmd):
    cmd_str = []
    for word in cmd:
        cmd_str.append(str(word))
    return ' '.join(cmd_str)


test = False
test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

cmd_cycles = {'noop': 1, 'addx': 2}
X = 1
signal_strengths = []
cycle = 1

for cmd in map(lambda x: x.strip().split(), file_lines):
    op = cmd[0]
    val = 0 if op == 'noop' else int(cmd[1])
    num_cycles = cmd_cycles[op]
    for cycle_step in range(num_cycles):
        signal_strength = cycle * X
        signal_strengths.append(signal_strength)
        print(f"cycle {cycle:<5} {' '.join(cmd):10}, signal strength: {signal_strength:<5}, start_X: {X:<3}", end="")
        if cycle_step == num_cycles - 1:
            # Last cycle for operation
            X += val
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