"""
Advent of Code 2022
Day 13

"""
from helpers.io import read_input
import numpy as np
import copy
import sys

debug = False


X_LEFT = -2
Y_LOWER = 0


class Raster():
    def __init__(self, lines):
        self.build(lines)

    def plot(self, extra_border=False, shift_back=True):
        # plot
        np_min_x = 0
        np_min_y = 0
        np_max_x = self.raster.shape[0] - 1
        np_max_y = self.raster.shape[1] - 1
        if shift_back:
            min_x = X_LEFT
            max_x = np_max_x + X_LEFT
        else:
            min_x = 0
            max_x = np_max_x

        if extra_border:
            min_y = 0
            max_y = self.raster.shape[1] - 1
        else:
            min_y = 0
            max_y = self.raster.shape[1] - 1

        # print header (x values)
        no_of_header_rows = len(str(max_x))
        header_prefix = len(f"{max_x:02} ") * ' '
        for header_row in range(no_of_header_rows):
            print(header_prefix, end="")
            digit_index = no_of_header_rows - header_row - 1
            for x_loc in range(min_x, max_x + 1):
                x_loc_str_inv = str(abs(x_loc))[::-1]
                display_digit = x_loc_str_inv[digit_index] if len(x_loc_str_inv) > digit_index else None
                mod5 = (x_loc % 5 == 0)
                if display_digit and mod5:
                    print(display_digit, end="")
                else:
                    print('.', end="")
            print()

        for y in range(np_min_y, np_max_y + 1):
            print(f"{y:02} ", end="")
            for x in range(np_min_x, np_max_x + 1):
                if self.raster[x, y] == 0:
                    print('.', end="")
                elif self.raster[x, y] == 1:
                    print('S', end="")
                else:
                    # self.raster[row, x] == 2:
                    print('B', end="")
            print()

    def build(self, lines):
        # use numpy 2 dimensional array
        # problem is that the sand goes down, but up the Y-axis values
        # and the x values do not start at 0, (and numpy indices always start at 0)
        #   so x values will be shifted to 0
        #   and sand flows up instead of down...
        sensors_and_beacons = []
        for line in lines:
            sensor_coord_y = int(line.split(':')[0].split(',')[1].split('=')[1])
            sensor_coord_x = int(line.split(':')[0].split(',')[0].split('=')[1])
            closest_beacon_y = int(line.split(':')[1].split(',')[1].split('=')[1])
            closest_beacon_x = int(line.split(':')[1].split(',')[0].split('=')[1])
            sensors_and_beacons.append([(sensor_coord_x, sensor_coord_y), (closest_beacon_x, closest_beacon_y)])
        x_left, x_right, y_upper, y_lower = get_bounds(sensors_and_beacons)

        raster = np.zeros((x_right - x_left + 1, y_upper - y_lower + 1), int)
        for sensor_bacon in sensors_and_beacons:
            sensor_coords = shift_coord(sensor_bacon[0])
            beacon_coords = shift_coord(sensor_bacon[1])
            raster[sensor_coords[0], sensor_coords[1]] = 1
            raster[beacon_coords[0], beacon_coords[1]] = 2
        self.raster = raster


def shift_coord(coord, x_left = X_LEFT, y_lower = Y_LOWER):
    shift_x = coord[0] - x_left
    shift_y = coord[1] - y_lower
    return (shift_x, shift_y)


def get_bounds(coordinate_sets):
    x_left = None
    x_right = None
    y_upper = None
    y_lower = None
    for coord_set in coordinate_sets:
        for coord in coord_set:
            coord_shifted = shift_coord(coord)
            x_left = coord_shifted[0] if x_left == None else min(x_left, coord_shifted[0])
            x_right = coord_shifted[0] if x_right == None else max(x_right, coord_shifted[0])
            y_upper = coord_shifted[1] if y_upper == None else max(y_upper, coord_shifted[1])
            y_lower = coord_shifted[1] if y_lower == None else min(y_lower, coord_shifted[1])
    return x_left, x_right, y_upper, y_lower


def build_raster(lines):
    # use numpy 2 dimensional array
    # problem is that the sand goes down, but up the Y-axis values
    # and the x values do not start at 0, (and numpy indices always start at 0)
    #   so x values will be shifted to 0
    #   and sand flows up instead of down...
    sensors_and_beacons = []
    for line in lines:
        sensor_coord_y = int(line.split(':')[0].split(',')[1].split('=')[1])
        sensor_coord_x = int(line.split(':')[0].split(',')[0].split('=')[1])
        closest_beacon_y = int(line.split(':')[1].split(',')[1].split('=')[1])
        closest_beacon_x = int(line.split(':')[1].split(',')[0].split('=')[1])
        sensors_and_beacons.append([(sensor_coord_x, sensor_coord_y), (closest_beacon_x, closest_beacon_y)])
    x_left, x_right, y_upper, y_lower = get_bounds(sensors_and_beacons)

    raster = np.zeros((x_right - x_left + 1, y_upper - y_lower + 1), int)
    for sensor_bacon in sensors_and_beacons:
        sensor_coords = shift_coord(sensor_bacon[0])
        beacon_coords = shift_coord(sensor_bacon[1])
        raster[sensor_coords[0], sensor_coords[1]] = 1
        raster[beacon_coords[0], beacon_coords[1]] = 2
    return raster


def display_raster(raster, extra_border=False, shift_back=False):
    if shift_back:
        min_x = X_LEFT
        max_x = raster.shape[0] + X_LEFT
    else:
        min_x = 0
        max_x = raster.shape[0]

    if extra_border:
        min_y = 0
        max_y = raster.shape[1] - 1
    else:
        min_y = 1
        max_y = raster.shape[1]

    # print header (x values)
    no_of_header_rows = len(str(max_x))
    header_prefix = len(f"{max_x:02} ") * ' '
    for header_row in range(no_of_header_rows):
        print(header_prefix, end="")
        digit_index = no_of_header_rows - header_row - 1
        for x_loc in range(min_x, max_x + 1):
            x_loc_str_inv = str(abs(x_loc))[::-1]
            display_digit = x_loc_str_inv[digit_index] if len(x_loc_str_inv) > digit_index else None
            mod5 = (x_loc % 5 == 0)
            if display_digit and mod5:
                print(display_digit, end="")
            else:
                print('.', end="")
        print()

    for x in range(min_x, max_x + 1):
        print(f"{x:02} ", end="")
        for row in range(raster.shape[0]-1):
            if raster[row, x] == 0:
                print('.', end="")
            elif raster[row, x] == 1:
                print('S', end="")
            else:
                # raster[row, x] == 2:
                print('B', end="")
        print()


# ======================================
# MAIN
# ======================================

test = False
test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
raster = Raster(file_lines)
raster.plot()

print('finished')
