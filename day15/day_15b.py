"""
Advent of Code 2022
Day 15
"""
from helpers.io import read_input
from shapely.geometry import Polygon
from shapely.ops import unary_union
import matplotlib.pyplot as plt
import shapely.geometry.multipolygon

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
        dist = man_dist(sensor_coord, beacon_coord)
        left_coord = (sensor_coord[0] - dist, sensor_coord[1])
        right_coord = (sensor_coord[0] + dist, sensor_coord[1])
        upper_coord = (sensor_coord[0], sensor_coord[1] - dist)
        lower_coord = (sensor_coord[0], sensor_coord[1] + dist)
        sensors[sensor_coord] = Polygon([left_coord, upper_coord, right_coord, lower_coord])
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


def merge_areas(sensors):
    total_area = None
    for sensor_coord, sensor_area in sensors.items():
        print(f"Adding sensor's {sensor_coord} area ...")
        if not total_area:
            total_area = sensor_area
        else:
            total_area = unary_union([total_area, sensor_area])
    return total_area

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

if False:
    for p in sensors.values():
        plt.plot(*p.exterior.xy)
    plt.show()

total_area = merge_areas(sensors)
print()

plot_result = False
if isinstance(total_area, shapely.geometry.multipolygon.MultiPolygon):
    for poly1 in total_area.geoms:
        if plot_result:
            plt.plot(*poly1.exterior.xy, color='green')
        for poly_int in poly1.interiors:
            if plot_result:
                plt.plot(*poly_int.xy, color='red')
else:
    if plot_result:
        plt.plot(*total_area.exterior.xy, color='green')
    for poly_int in total_area.interiors:
        if plot_result:
            plt.plot(*poly_int.xy, color='red')
if plot_result:
    plt.show()

# oke ik hou uiteindelijk maar 1 interior over !!
# POLYGON ((2843632 2948437, 2843634 2948437, 2843634 2948439, 2843632 2948439, 2843632 2948437))
# hieruit kan ik handmatig het overgebleven punt uit afleiden en daarna de 'tuning frequency' berekenen
# 2843633*4000000 + 2948438
# 11374534948438
# HAHAHA verrek het is nog goed ook, LOL
print('Done!')
