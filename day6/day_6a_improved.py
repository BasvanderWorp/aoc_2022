"""
Advent of Code 2022
Day 6

"""
from helpers.io import read_input, split_list

lines = read_input('input')
# marker_len = 4 # 6a
marker_len = 14 # 6b
first_marker = min([index + marker_len for line in lines for index in range(len(line)) if
              len(set(line[index:index+marker_len])) == marker_len])
print(first_marker)
