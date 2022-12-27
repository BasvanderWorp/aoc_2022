"""
Advent of Code 2022
Day 13

"""
from helpers.io import read_input
import numpy as np
import copy

def convert_to_string(item):
    if isinstance(item, list):
        if len(item) > 0:
            result = convert_to_string(item[0])
        else:
            result = '0'

        if len(item) > 1:
            result += convert_to_string(item[1:])
        return result
    else:
        # item is int
        result = str(item)
        return result

def smaller_than(left_item, right_item):
    if isinstance(left_item, list):
        if isinstance(right_item, list):
            if len(left_item) > 0:
                if len(right_item) > 0:
                    result = smaller_than(left_item[0], right_item[0])
                else:
                    result = False
            elif len(right_item) > 0:
                result = True
            else:
                # both are empty, return equal
                result = None

            if result == None:
                if len(left_item) > 1:
                    if len(right_item) > 1:
                        result = smaller_than(left_item[1:], right_item[1:])
                    else:
                        result = False
                elif len(right_item) > 1:
                    result = True
                else:
                    result = None
            return result
        else:
            # left is list, right is int
            result = smaller_than(left_item, [right_item])
            return result
    else:
        if isinstance(right_item, list):
            # left is int, right is list
            result = smaller_than([left_item], right_item)
            return result
        else:
            # both ints
            if left_item == right_item:
                result = None
            else:
                result = left_item < right_item
            return result


# ======================================
# MAIN
# ======================================
test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
lines = read_input(input_file)

items = [eval(line) for idx, line in enumerate(lines) if line != '']

right_order_bool = np.array([], bool)
right_order_bool_rev = np.array([], bool)
right_order_indices = []
sorted_items = [[[2]], [[6]]]
for i, p in enumerate(items):
    idx = 0
    for item in sorted_items:
        if smaller_than(p, item):
            break
        else:
            idx += 1
    sorted_items.insert(idx, p)

print(f"Decoder key: {(sorted_items.index([[2]]) + 1) * (sorted_items.index([[6]]) + 1)}")
print()

