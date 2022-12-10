"""
Advent of Code 2022
Day 8

"""
from helpers.io import read_input, split_list
import numpy as np

# numpy array
def read_trees(lines):
    tree_list_of_lists = []
    for line in lines:
        tree_list_of_lists.append(list(line))
    tree_arr = np.array(tree_list_of_lists)
    return tree_arr

def get_scenic_score(tree, tree_row, direction):
    if direction == 'right':
        tree_index = len(tree_row) - 1
        sc_score = 1
        blocked = tree_row[tree_index] >= tree
        while tree_index > 0 and not blocked:
            tree_index -= 1
            blocked = tree_row[tree_index] >= tree
            sc_score += 1
    else:
        tree_index = 0
        sc_score = 1
        blocked = tree_row[tree_index] >= tree
        while tree_index < len(tree_row) - 1 and not blocked:
            tree_index += 1
            blocked = tree_row[tree_index] >= tree
            sc_score += 1
    return sc_score


def get_highest_scenic_score(tree_arr):
    max_scenic_score = 0
    # borders
    rows = tree_arr.shape[0]
    cols = tree_arr.shape[1]
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            tree = tree_arr[row, col]
            tree_row = tree_arr[row,:]
            tree_col = tree_arr[:,col]
            scenic_score_left = get_scenic_score(tree, tree_row[:col], 'right')
            scenic_score_right = get_scenic_score(tree, tree_row[col+1:], 'left')
            scenic_score_up = get_scenic_score(tree, tree_col[row+1:], 'left')
            scenic_score_down = get_scenic_score(tree, tree_col[:row], 'right')
            scenic_score = scenic_score_left * scenic_score_right * scenic_score_up * scenic_score_down
            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score


test = False
#test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

tree_array = read_trees(file_lines)
sc_score = get_highest_scenic_score(tree_array)

print(sc_score)

