"""
Advent of Code 2022
Day 9

"""
from helpers.io import read_input, split_list
import numpy as np


# numpy array
def read_moves(lines):
    steps = []
    for line in lines:
        steps.append([line.split(' ')[0], line.split(' ')[1]])
    return steps


def distance(pos1, pos2):
    dist = (abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))
    sum_dist = (max(dist))
    return sum_dist, dist


def move_head(pos, step):
    if step[0] == 'R':
        new_pos = (pos[0] + 1, pos[1])
    elif step[0] == 'U':
        new_pos = (pos[0], pos[1] + 1)
    elif step[0] == 'L':
        new_pos = (pos[0] - 1, pos[1])
    elif step[0] == 'D':
        new_pos = (pos[0], pos[1] - 1)
    return new_pos


def move_tail(pos_tail, pos_head):
    if pos_tail[0] < pos_head[0]:
        if pos_tail[1] < pos_head[1]:
            # diagonal right up
            pos_tail = (pos_tail[0] + 1, pos_tail[1] + 1)
        elif pos_tail[1] > pos_head[1]:
            # diagonal right down
            pos_tail = (pos_tail[0] + 1, pos_tail[1] - 1)
        else:
            # not possible in 9a?
            pos_tail = (pos_tail[0] + 1, pos_tail[1])
    elif pos_tail[0] > pos_head[0]:
        if pos_tail[1] < pos_head[1]:
            # diagonal right up
            pos_tail = (pos_tail[0] - 1, pos_tail[1] + 1)
        elif pos_tail[1] > pos_head[1]:
            # diagonal right down
            pos_tail = (pos_tail[0] - 1, pos_tail[1] - 1)
        else:
            # not possible in 9a?
            pos_tail = (pos_tail[0] - 1, pos_tail[1])
    else:
        if pos_tail[1] < pos_head[1]:
            # right up
            pos_tail = (pos_tail[0], pos_tail[1] + 1)
        elif pos_tail[1] > pos_head[1]:
            # right down
            pos_tail = (pos_tail[0], pos_tail[1] - 1)
        else:
            # not possible in 9a?
            pass
    return pos_tail


test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
moves = read_moves(file_lines)

h_pos= (0,0)
t_pos= (0,0)
visited = [t_pos]
for move in moves:
    for step_counter in range(int(move[1])):
        step = [move[0], 1]
        h_pos = move_head(h_pos, step)
        print(h_pos, end="")
        sum_dist, dist = distance(h_pos, t_pos)
        if sum_dist < 2:
            # do nothing
            pass
            print()
        else:
            if h_pos == (0, -6):
                dummy = 'nothing'
            t_pos = move_tail(t_pos, h_pos)
            print(t_pos)
            visited.append(t_pos)
print(len(set(visited)))



print('finished')

