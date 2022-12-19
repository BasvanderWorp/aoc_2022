"""
Advent of Code 2022
Day 17
TETRIS HAHA

"""
from helpers.io import read_input, split_list
import numpy as np
import copy


class Rock():
    def __init__(self, rock_coords:np.array):
        # shape is a matrix with 1's (#'s) and 0's (.'s)
        self.rock = rock_coords
        # pos indicates the position of the left upper coordinate, always starts
        self.pos = (0, 2)
        self.calc_edges()
        self.width = self.rock.shape[1]
        self.height = self.rock.shape[0]

    def calc_edges(self):
        self.pos_upper_left = self.pos
        self.pos_lower_left = (self.pos_upper_left[0] + self.rock.shape[0] - 1, self.pos_upper_left[1])
        self.pos_upper_right = (self.pos_upper_left[0], self.pos_upper_left[1] + self.rock.shape[1] - 1)
        self.pos_lower_right = (self.pos_lower_left[0], self.pos_upper_right[1])

    def move(self, direction, dist):
        if direction == '>':
            dir_shift = (0, dist)
        elif direction == '<':
            dir_shift = (0, -dist)
        elif direction == 'v':
            dir_shift = (dist, 0)
        self.pos = tuple([sum(x) for x in zip(self.pos, dir_shift)])
        self.calc_edges()


class Raster():
    def __init__(self):
        # initialize raster on 3 rows (x-coord) and 7 columns (y-coord)
        self.raster = np.zeros((3, 7), int)
        self.raster_upper_row = 0
        self.raster_height = self.raster.shape[0]
        self.rock_total_height = 0
        self.rocks_stopped = True
        self.dir_map = {'>': (0, 1), '<': (0, -1), 'v': (1,0)}

    def add_rock(self, rock:Rock):
        self.falling_rock = copy.copy(rock)

        # clear all empty lines on top of raster
        number_of_empty_lines = 0
        for line in self.raster:
            if sum(line) == 0:
                number_of_empty_lines += 1
            else:
                break
        if number_of_empty_lines == self.raster.shape[0]:
            # raster is empty
            self.raster = np.zeros((self.falling_rock.height + 3, 7), int)
        else:
            self.raster = np.concatenate((np.zeros((self.falling_rock.height + 3, 7), int),
                                         self.raster[number_of_empty_lines:]))

        for x_coord in range(rock.rock.shape[0]):
            for y_coord in range(rock.rock.shape[1]):
                self.raster[x_coord, y_coord + 2] = rock.rock[x_coord, y_coord]

    def calc_total_height(self):
        # calc_total_height
        number_of_empty_lines = 0
        for line in self.raster:
            if sum(line) == 0:
                number_of_empty_lines += 1
            else:
                break
        if number_of_empty_lines == self.raster.shape[0]:
            # raster is empty
            self.rock_total_height = 0
        else:
            self.rock_total_height = self.raster.shape[0] - number_of_empty_lines

    def clear_falling_rock(self):
        for x_coord in range(self.falling_rock.height):
            for y_coord in range(self.falling_rock.width):
                raster_pos = tuple([sum(c) for c in zip(self.falling_rock.pos, (x_coord, y_coord))])
                if self.falling_rock.rock[x_coord, y_coord] == 1:
                    self.raster[raster_pos] = 0

    def rock_can_be_moved(self, direction):
        can_be_moved = True

        new_left_upper_pos = tuple([sum(x) for x in zip(self.falling_rock.pos,
                                                        self.dir_map[direction])])
        new_right_lower_pos = tuple([sum(x) for x in zip(new_left_upper_pos,
                                                         self.falling_rock.rock.shape)])
        raster_projected = self.raster[new_left_upper_pos[0]:new_right_lower_pos[0],
                           new_left_upper_pos[1]:new_right_lower_pos[1]]
        if np.amax(self.falling_rock.rock + raster_projected) > 1:
            can_be_moved = False
        # for x_coord in range(self.falling_rock.height):
        #     for y_coord in range(self.falling_rock.width):
        #         old_raster_pos = tuple([sum(c) for c in zip(self.falling_rock.pos, (x_coord, y_coord))])
        #         new_raster_pos = tuple([sum(c) for c in zip(old_raster_pos, self.dir_map[direction])])
        #         if self.falling_rock.rock[x_coord, y_coord] + self.raster[new_raster_pos] > 1:
        #             can_be_moved = False
        return can_be_moved

    def place_rock(self, offset):
        for x_coord in range(self.falling_rock.height):
            for y_coord in range(self.falling_rock.width):
                pos = tuple([sum(c) for c in zip(offset, (x_coord, y_coord))])
                if self.falling_rock.rock[x_coord, y_coord] == 1:
                    self.raster[pos] = 1

    def move_rock(self, direction):
        rock_moved = False
        if direction == '>':
            # to the right, check if right border has not been reached and if it can be moved
            curr_right_y_pos = self.falling_rock.pos_upper_right[1]
            new_right_y_pos = curr_right_y_pos + 1
            if new_right_y_pos < self.raster.shape[1]:
                old_pos = self.falling_rock.pos
                new_pos = tuple([sum(x) for x in zip(self.falling_rock.pos, self.dir_map[direction])])
                self.clear_falling_rock()
                if self.rock_can_be_moved(direction):
                    self.place_rock(new_pos)
                    rock_moved = True
                    self.falling_rock.move(direction, 1)
                else:
                    self.place_rock(old_pos)
        elif direction == '<':
            # to the left, check if left border has not been reached and if it can be moved
            curr_left_y_pos = self.falling_rock.pos_upper_left[1]
            new_left_y_pos = curr_left_y_pos - 1
            if new_left_y_pos >= 0:
                old_pos = self.falling_rock.pos
                new_pos = tuple([sum(x) for x in zip(self.falling_rock.pos, self.dir_map[direction])])
                self.clear_falling_rock()
                if self.rock_can_be_moved(direction):
                    self.place_rock(new_pos)
                    rock_moved = True
                    self.falling_rock.move(direction, 1)
                else:
                    self.place_rock(old_pos)
        # Now move down
        direction = 'v'
        curr_lower_x = self.falling_rock.pos_lower_left[0]
        new_lower_x_pos = curr_lower_x + 1
        if new_lower_x_pos < self.raster.shape[0]:
            old_pos = self.falling_rock.pos
            new_pos = tuple([sum(x) for x in zip(self.falling_rock.pos, self.dir_map[direction])])
            self.clear_falling_rock()
            if self.rock_can_be_moved(direction):
                self.place_rock(new_pos)
                rock_moved = True
                self.falling_rock.move(direction, 1)
                self.rocks_stopped = False
            else:
                self.place_rock(old_pos)
                self.rocks_stopped = True
        else:
            self.rocks_stopped = True
        return rock_moved

    def display(self, max_rows=20):
        for x in range(min(self.raster.shape[0], max_rows)):
            for y in range(self.raster.shape[1]):
                if self.raster[x, y] == 0:
                    print('.', end="")
                else:
                    print(u"\u2588", end="")
            print()

test = False
test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
moves = file_lines[0]
raster = Raster()

plot = False
debug_per_move = False
rocks = []

rock1_coords = np.array([[1, 1, 1, 1]], int)
rocks.append(Rock(rock1_coords))
rock2_coords = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], int)
rocks.append(Rock(rock2_coords))
rock3_coords = np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]], int)
rocks.append(Rock(rock3_coords))
rock4_coords = np.array([[1], [1], [1], [1]], int)
rocks.append(Rock(rock4_coords))
rock5_coords = np.array([[1, 1], [1, 1]], int)
rocks.append(Rock(rock5_coords))

next_rock_index = 0
next_move_index = 0
rock_number = 0
raster.calc_total_height()

# TODO add test raster data
# test 1: down
# raster.raster = np.concatenate((raster.raster, np.array([[0,0,0,0,1,1,1],
#                                 [0,0,0,0,0,1,1], [0,0,0,0,1,1,1], [0,0,0,0,1,1,1]], int)))
# moves = '<<<<<>>>'
# next_rock_index = 1

# test 2: right
# replace rock 2
# rock_test_coords = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]], int)
# rocks[2] = Rock(rock_test_coords)
# raster.raster = np.concatenate((raster.raster, np.array([[1,0,1,0,1,1,1],
#                                 [1,0,0,0,1,1,1], [1,0,0,0,1,1,1], [1,0,0,0,1,1,1]], int)))
# moves = '<<<>>>'
# next_rock_index = 2

# test 3: left
# replace rock 2
# rock_test_coords = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]], int)
# rocks[2] = Rock(rock_test_coords)
# raster.raster = np.concatenate((raster.raster, np.array([[1,0,1,0,1,1,1],
#                                 [1,0,0,0,1,1,1], [1,0,0,0,1,1,1], [1,0,0,0,1,1,1]], int)))
# moves = '<>><>>'
# next_rock_index = 2

# test 4: left
# replace rock 2
# rock_test_coords = np.array([[1, 1, 1], [1, 0, 0], [1, 0, 0]], int)
# rocks[2] = Rock(rock_test_coords)
# raster.raster = np.concatenate((raster.raster, np.array([[1,0,1,1,0,1,1],
#                                 [1,0,0,0,0,1,1], [1,0,0,0,0,1,1], [1,0,0,0,0,1,1]], int)))
# moves = '<>>>>>'
# next_rock_index = 2


raster.add_rock(rocks[next_rock_index])
raster.rocks_stopped = False
rock_number += 1
next_rock_index = (next_rock_index + 1) % 5

# print(f'rock number {rock_number}')

if plot:
    raster.display()

last_rock = 2022
# last_rock = 1000000000000
while rock_number < last_rock or not raster.rocks_stopped:
    next_move = moves[next_move_index]
    next_move_index = (next_move_index + 1) % len(moves)
    if raster.rocks_stopped:
        raster.calc_total_height()
        if rock_number % 10000 == 0:
            print(f'rock number {rock_number}')
        if rock_number == last_rock:
            break
        raster.add_rock(rocks[next_rock_index])
        if plot:
            print()
            raster.display()
        rock_number += 1
        next_rock_index = (next_rock_index + 1) % 5
    if plot and debug_per_move:
        print()
        print(f"next move: {next_move}")
    raster.move_rock(next_move)
    if plot and debug_per_move:
        raster.display()

raster.calc_total_height()
print(raster.rock_total_height)

print('finished')
