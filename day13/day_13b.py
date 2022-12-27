"""
Advent of Code 2022
Day 13

"""
from helpers.io import read_input
import numpy as np
import copy

def right_order(left_item, right_item):
    if isinstance(left_item, list):
        if isinstance(right_item, list):
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
            if left_item == right_item:
                result = 'equal'
            else:
                result = 'true' if left_item < right_item else 'false'
            return result


# ======================================
# MAIN
# ======================================
test = False
# test = True
input_file = 'input.txt' if not test else 'input_test.txt'
lines = read_input(input_file)

pairs = list(zip([eval(line) for idx, line in enumerate(lines) if idx % 3 == 0],
                 [eval(line) for idx, line in enumerate(lines) if (idx - 1) % 3 == 0]))

right_order_indices = []
for i, p in enumerate(pairs):
    if right_order(p[0], p[1]) == 'true':
        right_order_indices.append(i+1)

print(f"Indices: {right_order_indices}")
print()
print(f"som: {sum(right_order_indices)}")
