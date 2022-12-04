
calories = []
cal_set = []
with open('input.txt', 'r') as f:
    for line in f:
        if line != '\n':
            cal_set.append(int(line.split('\n')[0]))
        else:
            calories.append(cal_set)
            cal_set = []

max_cals = max([sum(cal_set) for cal_set in calories])
print(max_cals)
