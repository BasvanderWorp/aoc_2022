"""
Advent of Code 2022
Day 14

"""
from helpers.io import read_input
import numpy as np
import copy
import sys

def build_raster(lines, pouring_coord):
    # use dictionary
    raster = {}
    for line in lines:
        path = []
        path_raw = line.strip().split('->')
        prev_coord = ()
        for coord_raw in path_raw:
            coord = tuple(int(c) for c in coord_raw.strip().split(','))
            if prev_coord:
                start_x = min(prev_coord[0], coord[0])
                end_x = max(prev_coord[0], coord[0])
                start_y = min(prev_coord[1], coord[1])
                end_y = max(prev_coord[1], coord[1])
                for x in range(start_x, end_x + 1):
                    for y in range(start_y, end_y + 1):
                        raster[x, y] = '#'
                prev_coord = coord
            else:
                raster[coord[0], coord[1]] = '#'
                prev_coord = coord
    return raster, get_abyss(raster) + 2

def get_abyss(raster):
    abyss = 0
    for coord in raster.keys():
        abyss = max(abyss, coord[1])
    return abyss

def drop(raster, coord, bottom):
    next_pos = (coord[0], coord[1] + 1)
    if next_pos[1] == bottom:
        raster[coord] = 'o'
        return coord
    else:
        if next_pos not in raster.keys():
            return next_pos
        else:
            next_pos = (coord[0] - 1, coord[1] + 1)
            if next_pos not in raster.keys():
                return next_pos
            else:
                next_pos = (coord[0] + 1, coord[1] + 1)
                if next_pos not in raster.keys():
                    return next_pos
                else:
                    raster[coord] = 'o'
                    return coord

def drop_sand(raster, abyss, pour_coord):
    # criterium: if sand drops below lowest line it drops in the abyss
    #   in that case, stop. That last unit of sand does not count, and raster is not updated
    sand_unit = pour_coord
    while pour_coord not in raster.keys():
        new_pos = drop(raster, sand_unit, bottom)
        if sand_unit == new_pos:
            sand_unit = pour_coord
        else:
            sand_unit = new_pos
    return raster

# ======================================
# MAIN
# ======================================

test = False
#test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
sand_pour_coord = (500, 0)
raster, bottom = build_raster(file_lines, sand_pour_coord)
raster = drop_sand(raster, bottom, sand_pour_coord)
sandunits = sum([1 for x in raster.values() if x == 'o'])
print(sandunits)
