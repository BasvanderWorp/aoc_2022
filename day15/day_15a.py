"""
Advent of Code 2022
Day 15

"""
from helpers.io import read_input
import numpy as np
import copy
import sys

def read_sensors(lines: list):
    sensors = {}
    beacons = []
    for line in lines:
        sensor_data = line.split(':')[0]
        beacon_data = line.split(':')[1]
        sensor_coord = (int(sensor_data.split(',')[0].split('=')[1]),
                        int(sensor_data.split(',')[1].split('=')[1]))
        beacon_coord = (int(beacon_data.split(',')[0].split('=')[1]),
                        int(beacon_data.split(',')[1].split('=')[1]))
        beacons.append(beacon_coord)
        # sensors[(int(sensor_x), int(sensor_y))] = (int(beacon_x), int(beacon_y))
        sensors[sensor_coord] = man_dist(sensor_coord, beacon_coord)
    return sensors, beacons

def man_dist(coord1, coord2):
    dist_x = abs(coord1[0] - coord2[0])
    dist_y = abs(coord1[1] - coord2[1])
    return dist_x + dist_y

def get_x_bounds(sensors):
    x_min = list(sensors.keys())[0][0]
    x_max = x_min
    for sensor, sensor_range in sensors.items():
        x_min = min(x_min, sensor[0] - sensor_range)
        x_max = max(x_max, sensor[0] + sensor_range)
    return x_min, x_max

def get_num_occupied_pos(sensors, beacons, x_bounds, y):
    num_occ_pos = 0
    prev_perc = -1
    for x in range(x_bounds[0], x_bounds[1] + 1):
        perc = round((x - x_bounds[0]) / (x_bounds[1] - x_bounds[0]) * 100)
        if perc % 5 == 0:
            if perc != prev_perc:
                print(f'{perc}%')
                prev_perc = perc

        x_checked = False
        for sensor_coord, sensor_range in sensors.items():
            if man_dist((x,y), sensor_coord) <= sensor_range and not x_checked and (x,y) not in beacons:
                num_occ_pos += 1
                # print(x, y)
                x_checked = True
        if False:
            if (x,y) in beacons:
                print('B', end="")
            elif x_checked:
                print('#', end="")
            else:
                print('.', end="")
    print()
    return num_occ_pos

# ======================================
# MAIN
# ======================================
test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

print('Start reading sensors and beacons')
sensors, beacons = read_sensors(file_lines)
print('Sensors and beacons read')
x_bounds = get_x_bounds(sensors)
print(f"x bounds: {x_bounds}, number of xes: {x_bounds[1]-x_bounds[0]}")

num = get_num_occupied_pos(sensors, beacons, x_bounds, 2000000)
print()
print(num)

print()
