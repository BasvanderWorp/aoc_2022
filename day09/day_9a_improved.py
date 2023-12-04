"""
Advent of Code 2022
Day 9

"""
from helpers.io import read_input, split_list
import numpy as np
import sys

test = False
#test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

sgn = lambda x: (x > 0) - (x < 0)
h, t = (0, 0), (0, 0)
dir = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
seen = {t}

for args in map(lambda x: x.strip().split(), file_lines):
    d, v = args[0], int(args[1])
    for _ in range(v):
        h = tuple(sum(x) for x in zip(h, dir[d]))
        dx, dy = h[0] - t[0], h[1] - t[1]
        if abs(dx) > 1 or abs(dy) > 1:
            t = tuple(sum(x) for x in zip(t, [sgn(dx), sgn(dy)]))
        seen.add(t)

print(len(seen))