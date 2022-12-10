"""
Advent of Code 2022
Day 8

"""
from helpers.io import read_input, split_list
import numpy as np


def read_trees(lines):
    tree_list_of_lists = []
    for line in lines:
        tree_list_of_lists.append(list(line))
    tree_arr = np.array(tree_list_of_lists)
    return tree_arr


def get_num_visible(tree_arr):
    # get borders (all visible)
    num_visible = tree_arr.shape[0] * 2 + tree_arr.shape[1] * 2 - 4

    # get visible innner items
    rows = tree_arr.shape[0]
    cols = tree_arr.shape[1]
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            tree = tree_arr[row, col]
            tree_row = tree_arr[row,:]
            tree_col = tree_arr[:,col]
            if max(tree_row[:col]) < tree or max(tree_row[col+1:]) < tree or max(tree_col[row+1:]) < tree \
                    or max(tree_col[:row]) < tree:
                        num_visible += 1
    return num_visible


test = False
test = True
input_file = 'input.txt' if not test else 'input_test.txt'

file_lines = read_input(input_file)
tree_array = read_trees(file_lines)
num_vis = get_num_visible(tree_array)

print(num_vis)

