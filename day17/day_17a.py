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
        if direction == 'right':
            dir = (0, dist)
        elif direction == 'left':
            dir = (0, -dist)
        elif direction == 'down':
            dir = (dist, 0)
        self.pos = tuple([sum(x) for x in zip(self.pos, dir)])
        self.calc_edges()


class Raster():
    def __init__(self):
        # initialize raster on 3 rows (x-coord) and 7 columns (y-coord)
        self.raster = np.zeros((3, 7), int)
        self.raster_upper_row = 0
        self.raster_height = self.raster.shape[0]
        self.rock_total_height = 0
        self.rocks_stopped = True

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

    def move_rock(self, direction):
        rock_moved_left = False
        rock_moved_right = False
        rock_moved_down = False
        can_be_placed = True
        x_offset = self.falling_rock.pos[0]
        y_offset = self.falling_rock.pos[1]
        if direction == '>':
            # to the right, check if right border has not been reached and if can be moved
            curr_y = self.falling_rock.pos_upper_right[1]
            new_y = curr_y + 1
            can_be_placed = True
            if new_y < self.raster.shape[1]:
                for x_coord in range(self.falling_rock.height):
                    if self.falling_rock.rock[x_coord, self.falling_rock.width - 1] + \
                            self.raster[x_offset + x_coord, new_y] > 1:
                        can_be_placed = False
            else:
                can_be_placed = False
            if can_be_placed:
                # update raster by moving rock to the right
                # do this column by colum from right to the left
                for y_coord in range(self.falling_rock.width - 1, -1, -1):
                    for x_coord in range(self.falling_rock.height):
                        # update raster coord new column
                        x_pos = x_coord + x_offset
                        y_pos = y_coord + y_offset
                        y_new_pos = y_pos + 1
                        if self.falling_rock.rock[x_coord, y_coord] == 1:
                            self.raster[x_pos, y_new_pos] = 1
                        else:
                            # leave cell unchanged
                            pass
                        # update raster coord org column
                        if self.falling_rock.rock[x_coord, y_coord] == 1:
                            # if moved rock cell was rock, clear this cell
                            self.raster[x_pos, y_pos] = 0
                        else:
                            # leave cell unchanged
                            pass
                rock_moved_right = True
                self.falling_rock.move('right', 1)
        elif direction == '<':
            # to the left, check if left border has not been reached and if can be moved
            curr_y = self.falling_rock.pos_upper_left[1]
            new_y = curr_y - 1
            can_be_placed = True
            if new_y >= 0:
                for x_coord in range(self.falling_rock.height):
                    if self.falling_rock.rock[x_coord, 0] + \
                            self.raster[x_offset + x_coord, new_y] > 1:
                        can_be_placed = False
            else:
                can_be_placed = False
            if can_be_placed:
                # update raster by moving rock to the left
                # do this column by colum from left to right
                for y_coord in range(self.falling_rock.width):
                    for x_coord in range(self.falling_rock.height):
                        # update raster coord new column
                        x_pos = x_coord + x_offset
                        y_pos = y_coord + y_offset
                        y_new_pos = y_pos - 1
                        if self.falling_rock.rock[x_coord, y_coord] == 1:
                            self.raster[x_pos, y_new_pos] = 1
                        else:
                            # leave cell unchanged
                            pass
                        # update raster coord org column
                        if self.falling_rock.rock[x_coord, y_coord] == 1:
                            # if moved rock cell was rock, clear this cell
                            self.raster[x_pos, y_pos] = 0
                        else:
                            # leave cell unchanged
                            pass
                rock_moved_left = True
                self.falling_rock.move('left', 1)
        # Now move down
        # to the left, check if left border has not been reached and if can be moved
        can_be_placed = True
        x_offset = self.falling_rock.pos[0]
        y_offset = self.falling_rock.pos[1]
        curr_x = self.falling_rock.pos_lower_left[0]
        new_x = curr_x + 1
        can_be_placed = True
        if new_x < self.raster.shape[0]:
            for y_coord in range(self.falling_rock.width):
                if self.falling_rock.rock[self.falling_rock.height - 1, y_coord] + \
                        self.raster[new_x, y_offset + y_coord] > 1:
                    can_be_placed = False
        else:
            can_be_placed = False
        if can_be_placed:
            # update raster by moving rock down
            # do this row by row going up
            for x_coord in range(self.falling_rock.height - 1, -1, -1):
                for y_coord in range(self.falling_rock.width):
                    # update raster coord new row
                    x_pos = x_coord + x_offset
                    y_pos = y_coord + y_offset
                    x_new_pos = x_pos + 1
                    if self.falling_rock.rock[x_coord, y_coord] == 1:
                        self.raster[x_new_pos, y_pos] = 1
                    else:
                        # leave cell unchanged
                        pass
                    # update raster coord org column
                    if self.falling_rock.rock[x_coord, y_coord] == 1:
                        # if moved rock cell was rock, clear this cell
                        self.raster[x_pos, y_pos] = 0
                    else:
                        # leave cell unchanged
                        pass
            rock_moved_down = True
            self.falling_rock.move('down', 1)
        horizontal_move = ''
        vertical_move = ''
        rock_moved = False
        if rock_moved_right:
            horizontal_move = 'right'
            rock_moved = True
        elif rock_moved_left:
            horizontal_move = 'left'
            rock_moved = True
        if rock_moved_down:
            vertical_move = 'down'
            rock_moved = True
        # print(f'Rock moved ? : {horizontal_move}-{vertical_move}')
        if rock_moved_down:
            self.rocks_stopped = False
        else:
            self.rocks_stopped = True
        return rock_moved


    def expand_raster(self, num_y:int):
        new_rows_raw = []
        for x in range(num_y):
            new_rows_raw.append([0 for cols in range(7)])
        new_rows = np.array(new_rows_raw)
        self.raster = np.concatenate((new_rows, self.raster), axis=0)


test = False
test = True
input_file = 'input.txt' if not test else 'input_test2.txt'
file_lines = read_input(input_file)
moves = file_lines[0]
raster = Raster()

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
raster.add_rock(rocks[next_rock_index])
raster.rocks_stopped = False
rock_number += 1
next_rock_index = (next_rock_index + 1) % 5
print(f'rock number {rock_number}')
last_rock = 2022
while rock_number < last_rock or not raster.rocks_stopped:
    next_move = moves[next_move_index]
    next_move_index = (next_move_index + 1) % len(moves)
    if raster.rocks_stopped:
        raster.calc_total_height()
        if rock_number == last_rock:
            break
        raster.add_rock(rocks[next_rock_index])
        rock_number += 1
        print(f'rock number {rock_number}')
        next_rock_index = (next_rock_index + 1) % 5
    # TODO remove test
    if next_rock_index == 4:
        next_move = '<'
    else:
        next_move = '>'
    raster.move_rock(next_move)

raster.calc_total_height()
print(raster.rock_total_height)

print('finished')
