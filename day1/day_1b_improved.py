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

top_three = [0, 0, 0]
for idx, elf_cals in enumerate(calories):
    sum_elf_cals = sum(elf_cals)
    min_top_three = min(top_three)
    min_idx = top_three.index(min_top_three)
    if sum_elf_cals > min_top_three:
        top_three[min_idx] = sum_elf_cals

print(sum(top_three))