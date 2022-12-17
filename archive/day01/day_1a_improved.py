from helpers.io import read_input

calories = []
cal_set = []

calories = read_input('input.txt', dtype='int', sublists_on_newline=True)

max_cals = max([sum(cal_set) for cal_set in calories])
print(max_cals)
