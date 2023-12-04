"""
Advent of Code 2022
Day 9

"""
from helpers.io import read_input

test = False
# test = True
input_file = 'day09/input.txt' if not test else 'day09/input_test2.txt'
file_lines = read_input(input_file)

sgn = lambda x: (x > 0) - (x < 0)
dir = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
rope = [(0,0) for _ in range(10)]
seen = {rope[-1]}

for args in map(lambda x: x.strip().split(), file_lines):
    d, v = args[0], int(args[1])
    for _ in range(v):
        rope[0] = tuple(sum(x) for x in zip(rope[0], dir[d]))
        for i in range(1, len(rope)):
            dx, dy = rope[i - 1][0] - rope[i][0], rope[i - 1][1] - rope[i][1]
            if abs(dx) > 1 or abs(dy) > 1:
                rope[i] = tuple(sum(x) for x in zip(rope[i], (sgn(dx), sgn(dy))))
        seen.add(rope[-1])

print(len(seen))

print('finished')

