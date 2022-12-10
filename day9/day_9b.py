"""
Advent of Code 2022
Day 9

"""
from helpers.io import read_input, split_list
import copy


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
            new_pos_tail = (pos_tail[0] + 1, pos_tail[1] + 1)
        elif pos_tail[1] > pos_head[1]:
            # diagonal right down
            new_pos_tail = (pos_tail[0] + 1, pos_tail[1] - 1)
        else:
            # not possible in 9a?
            new_pos_tail = (pos_tail[0] + 1, pos_tail[1])
    elif pos_tail[0] > pos_head[0]:
        if pos_tail[1] < pos_head[1]:
            # diagonal right up
            new_pos_tail = (pos_tail[0] - 1, pos_tail[1] + 1)
        elif pos_tail[1] > pos_head[1]:
            # diagonal right down
            new_pos_tail = (pos_tail[0] - 1, pos_tail[1] - 1)
        else:
            # not possible in 9a?
            new_pos_tail = (pos_tail[0] - 1, pos_tail[1])
    else:
        if pos_tail[1] < pos_head[1]:
            # right up
            new_pos_tail = (pos_tail[0], pos_tail[1] + 1)
        elif pos_tail[1] > pos_head[1]:
            # right down
            new_pos_tail = (pos_tail[0], pos_tail[1] - 1)
        else:
            # not possible in 9a?
            pass
    return new_pos_tail


test = False
#test = True
input_file = 'input.txt' if not test else 'input_test2.txt'
file_lines = read_input(input_file)
moves = read_moves(file_lines)

rope_pos = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
# rope_pos[0] is the head
visited = [rope_pos[-1]]

for move in moves:
    for step_counter in range(int(move[1])):
        step = [move[0], 1]
        print(f"{rope_pos} ---", end="")
        rope_pos[0] = move_head(rope_pos[0], step)
        print(f"head to {rope_pos[0]} --- [{rope_pos[0], }", end="")
        if rope_pos[0] == (4, 2):
            dummy = 'nothing'
        for knot_idx in range(1,10):
            prev_knot = rope_pos[knot_idx-1]
            new_curr_knot = curr_knot = rope_pos[knot_idx]
            sum_dist, dist = distance(prev_knot, curr_knot)
            if sum_dist < 2:
                # do nothing
                pass
            else:
                if prev_knot == (4, 2):
                    dummy = 'nothing'
                new_curr_knot = move_tail(curr_knot, prev_knot)
            if new_curr_knot != curr_knot:
                rope_pos[knot_idx] = new_curr_knot
                print(f"{new_curr_knot}, ", end="")
            else:
                for idx in range(knot_idx + 1, 10):
                    print(f"{rope_pos[idx]}, ", end="")
                print("]")
                break
        visited.append(rope_pos[9])

print()
print()

print(len(set(visited)))

print('finished')

