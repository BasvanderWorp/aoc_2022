# Day 6
from helpers.io import read_input, split_list
lines = read_input('input')

# Single line of code, except for reading the input
print(min([idx + 14 for line in lines for idx in range(len(line)) if len(set(line[idx:idx+14])) == 14]))
