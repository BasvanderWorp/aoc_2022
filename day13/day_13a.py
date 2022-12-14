"""
Advent of Code 2022
Day 13

"""
from helpers.io import read_input
import numpy as np
import copy

debug = False


def read_pairs(lines):
    pairs = []
    idx = 0
    while idx < len(lines):
        left_item = eval(lines[idx])
        idx += 1
        right_item = eval(lines[idx])
        pairs.append((left_item, right_item))
        idx = min(idx + 2, len(lines))
    return pairs


def right_order(left_item, right_item):
    if isinstance(left_item, list):
        if isinstance(right_item, list):
            # both lists
            if len(left_item) > 0:
                if len(right_item) > 0:
                    result = right_order(left_item[0], right_item[0])
                else:
                    result = 'false'
            elif len(right_item) > 0:
                result = 'true'
            else:
                # both are empty, return equal
                result = 'equal'

            if result == 'equal':
                if len(left_item) > 1:
                    if len(right_item) > 1:
                        result = right_order(left_item[1:], right_item[1:])
                    else:
                        result = 'false'
                elif len(right_item) > 1:
                    result = 'true'
                else:
                    result = 'equal'
            return result
        else:
            # left is list, right is int
            result = right_order(left_item, [right_item])
            return result
    else:
        if isinstance(right_item, list):
            # left is int, right is list
            result = right_order([left_item], right_item)
            return result
        else:
            # both ints
            if left_item < right_item:
                result = 'true'
            elif left_item > right_item:
                result = 'false'
            else:
                result = 'equal'
            return result


# ======================================
# MAIN
# ======================================

test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)
pairs = read_pairs(file_lines)

right_order_bool = np.array([], bool)
right_order_bool_rev = np.array([], bool)
right_order_indices = []
for i, p in enumerate(pairs):
    print(f"regel {i*3+1} (index {i+1}): ", end="")
    if right_order(p[0], p[1]) == 'true':
        result = True
        print('true', end="")
        right_order_indices.append(i+1)
        right_order_bool = np.append(right_order_bool, True)
    else:
        result = False
        print('false', end="")
        right_order_bool = np.append(right_order_bool, False)

    if right_order(p[1], p[0]) == 'true':
        right_order_bool_rev = np.append(right_order_bool_rev, True)
        if result:
            print(' Result inverted does not match inverted result!')
        else:
            print()
    else:
        right_order_bool_rev = np.append(right_order_bool_rev, False)
        if not result:
            print(' Result inverted does not match inverted result!')
        else:
            print()

print(f"Indices: {right_order_indices}")
print()
print(f"som: {sum(right_order_indices)}")

print(f"Result inverted matches inverted result : {all(np.invert(right_order_bool) == right_order_bool_rev)}")

print('finished')
