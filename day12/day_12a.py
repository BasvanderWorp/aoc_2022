"""
Advent of Code 2022
Day 12

"""
from helpers.io import read_input
import numpy as np
import copy
import sys

paths_found = set()
debug = False

def get_ord(char):
    return ord(char) - ord('a')

def read_map(lines):
    map_tmp = []
    for line in lines:
        map_line = []
        for char in line:
            if char == 'S':
                hight = 0
            elif char == 'E':
                hight = ord('z') - ord('a')
            else:
                hight = ord(char) - ord('a')
            map_line.append(hight)
        map_tmp.append(map_line)
    map = np.array(map_tmp)
    return map


def get_neighbours(map, location):
    left_y = max(0, location[1]-1)
    right_y = min(map.shape[1]-1, location[1]+1)
    upper_x = max(0, location[0]-1)
    lower_x = min(map.shape[0]-1, location[0]+1)
    neigbours = []
    for x in range(upper_x, lower_x + 1):
        for y in range(left_y, right_y + 1):
            if (x, y) != location and not (x != location[0] and y != location[1]):
                neigbours.append((x, y))
    return neigbours


def find_dest(map, path, visited, dest, rec_level):
    # path is a list of coords
    # the last item is the current location
    # this recursive function ends if there are no more possibilities to climb or the destination has been reached
    cur_loc = path[-1]
    print(f'running, rec_level: {rec_level}, cur_loc: {cur_loc}, path: {path}')
    if str(path) in paths_found:
        print('duplicate path')
        sys.exit
    else:
        paths_found.add(str(path))
    neighbours = get_neighbours(map, cur_loc)
    found_paths = []
    org_path = copy.copy(path)
    org_visited = copy.copy(visited)
    for neighbour in neighbours:
        if map[neighbour] in [map[cur_loc], map[cur_loc]+1] and neighbour == dest:
            # Destination found
            spaces = rec_level * 2 * ' '
            if debug:
                print(f"{spaces}{neighbour}")
            is_valid = True
            path.append(neighbour)
            visited.append(cur_loc)
            found_paths.append(path)
            print(f"Path found: length {len(path)}: {path}")
            if len(path) == 60:
                print('stop')
            break
        if map[neighbour] in [map[cur_loc], map[cur_loc]+1] and neighbour not in visited:
            path = copy.copy(org_path)
            spaces = len(path) * 2 * ' '
            if debug:
                print(f"{spaces}{rec_level:6}: {neighbour} - {map[neighbour]} = {chr(ord('a') + map[neighbour])}")
            visited.append(cur_loc)
            path.append(neighbour)
            path_lengths = [len(path1) for path1 in found_paths]
            if not path_lengths or len(path) <= min(path_lengths):
                is_valid, new_found_paths = find_dest(map, path, visited, dest, rec_level + 1)
                if new_found_paths:
                    found_paths.extend(new_found_paths)
            else:
                is_valid = False
        else:
            is_valid = False
    return is_valid, found_paths


def print_path(path):
    grid = []
    x_dim = max([coord[0] for coord in path]) + 1
    y_dim = max([coord[1] for coord in path]) + 1
    grid = np.full((x_dim, y_dim), '.')
    prev_coord = path[0]
    for coord in path[1:]:
        if coord[0] - prev_coord[0] == 0:
            if coord[1] - prev_coord[1] == 1:
                grid[(prev_coord)] = '>'
            else:
                grid[(prev_coord)] = '<'
        elif coord[0] - prev_coord[0] == 1:
            grid[(prev_coord)] = 'v'
        elif coord[0] - prev_coord[0] == -1:
            grid[(prev_coord)] = '^'
        else:
            print('this cannot happen')
        prev_coord = coord
    print(grid)

def get_start_end(lines: list, letter):
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            if char == letter:
                return (x,y)
    return None

# ======================================
# MAIN
# ======================================

test = False
test = True
if test:
    input_file = 'input_test.txt'
else:
    input_file = 'input.txt'

file_lines = read_input(input_file)
S = get_start_end(file_lines, 'S')
E = get_start_end(file_lines, 'E')

map = read_map(file_lines)


# l1 = get_neighbours(map, (0,0))

count_print = 0
_, paths = find_dest(map, [S], [], E, 0)

print(min([len(path) for path in paths]) - 1)

shortest_paths = [path for path in paths if len(path) == min([len(p) for p in paths])]
for shortest_path in shortest_paths:
    print_path(shortest_path)
    print()

print('finished')
