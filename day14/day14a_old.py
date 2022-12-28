"""
Advent of Code 2022
Day 13

"""
from helpers.io import read_input
import numpy as np
import copy
import sys

debug = False

X_LEFT = 493
Y_LOWER = 0


def shift_coord(coord, x_left = X_LEFT, y_lower = Y_LOWER):
    shift_x = coord[0] - x_left
    shift_y = coord[1] - y_lower
    return (shift_x, shift_y)


def get_bounds(paths, extra_coord):
    x_left = None
    x_right = None
    y_upper = None
    y_lower = None
    for path in paths:
        for coord in path:
            coord_shifted = shift_coord(coord)
            x_left = coord_shifted[0] if x_left == None else min(x_left, coord_shifted[0])
            x_right = coord_shifted[0] if x_right == None else max(x_right, coord_shifted[0])
            y_upper = coord_shifted[1] if y_upper == None else max(y_upper, coord_shifted[1])
            y_lower = coord_shifted[1] if y_lower == None else min(y_lower, coord_shifted[1])
    # add sand
    x_left = min(x_left, extra_coord[0])
    x_right = max(x_right, extra_coord[0])
    y_upper = max(y_upper, extra_coord[1])
    y_lower = min(y_lower, extra_coord[1])
    # add 1 to left and right
    x_left -= 1
    x_right += 1
    return x_left, x_right, y_upper, y_lower


def build_raster(lines, pouring_coord):
    # use numpy 2 dimensional array
    # problem is that the sand goes down, but up the Y-axis values
    # and the x values do not start at 0, (and numpy indices always start at 0)
    #   so x values will be shifted to 0
    #   and sand flows up instead of down...
    paths = []
    for line in lines:
        path = []
        path_raw = line.strip().split('->')
        for coord_raw in path_raw:
            coord = coord_raw.strip().split(',')
            path.append((int(coord[0]), int(coord[1])))
        paths.append(path)
    x_left, x_right, y_upper, y_lower = get_bounds(paths, pouring_coord)

    raster = np.zeros((x_right - x_left + 1, y_upper - y_lower + 1), int)
    for path in paths:
        # first point
        coord = path[0]
        coord_shifted = shift_coord(coord)
        raster[coord_shifted] = 1
        prev_point = coord_shifted
        for next_point in path[1:]:
            shift_next_point = shift_coord(next_point)
            if shift_next_point[0] != prev_point[0]:
                if shift_next_point[1] != prev_point[1]:
                    print('ERROR: cannot draw diagonal')
                    sys.exit()
                # draw horizontal line
                min_x = min(prev_point[0], shift_next_point[0])
                max_x = max(prev_point[0], shift_next_point[0])
                for x in range(min_x, max_x + 1):
                    raster[x, shift_next_point[1]] = 1
            elif shift_next_point[1] != prev_point[1]:
                if shift_next_point[0] != prev_point[0]:
                    print('ERROR: cannot draw diagonal')
                    sys.exit()
                # draw horizontal line
                min_y = min(prev_point[1], shift_next_point[1])
                max_y = max(prev_point[1], shift_next_point[1])
                for y in range(min_y, max_y + 1):
                    raster[shift_next_point[0], y] = 1
            else:
                print('ERROR: same coordinate!')
            prev_point = shift_next_point
    return raster


def display_raster(raster, extra_border=True):
    if extra_border:
        min_y = 0
        max_y = raster.shape[1] - 1
    else:
        min_y = 1
        max_y = raster.shape[1]
    for col in range(min_y, max_y + 1):
        for row in range(raster.shape[0]-1):
            if raster[row, col] == 0:
                print('.', end="")
            elif raster[row, col] == 1:
                print('#', end="")
            else:
                # raster[row, col] == 2:
                print('o', end="")
        print()


def in_abyss(border, coord):
    return coord[1] > border


def drop(raster, coord):
    next_pos = raster[coord[0], coord[1] + 1]
    if next_pos == 0:
        return (coord[0], coord[1] + 1)
    elif next_pos in [1, 2]:
        diag_pos_left = raster[coord[0] - 1, coord[1] + 1]
        if diag_pos_left == 0:
            return (coord[0] - 1, coord[1] + 1)
        else:
            diag_pos_right = raster[coord[0] + 1, coord[1] + 1]
            if diag_pos_right == 0:
                return (coord[0] + 1, coord[1] + 1)
            else:
                # into rest position, return same coord
                return (coord[0], coord[1])


def update_raster(raster, pos):
    raster_updated = copy.copy(raster)
    raster_updated[pos[0], pos[1]] = 2


def drop_sand(raster, pour_coord):
    # criterium: if sand drops below lowest line it drops in the abyss
    #   in that case, stop. That last unit of sand does not count, and raster is not updated
    sand_unit = pour_coord
    while not in_abyss(raster.shape[1], sand_unit):
        new_pos = drop(raster, sand_unit)
        if sand_unit == new_pos:
            raster = update_raster(raster, new_pos)
            sand_unit = pour_coord
    return raster

# ======================================
# MAIN
# ======================================

test = False
test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
sand_pour_coord = shift_coord((500, 0))
raster = build_raster(file_lines, sand_pour_coord)
display_raster(raster)
raster = drop_sand(raster, sand_pour_coord)
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
