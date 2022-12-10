
with open('input.txt', 'r') as f:
    calories_raw = f.readlines()

# creat calories list
calories = []
first = True
for cal_item in calories_raw:
    cal = cal_item.split('\n')[0]
    if cal != '' and first == True:
        elf_cal = [int(cal)]
        first = False
    elif cal == '':
        calories.append(elf_cal)
        first = True
    else:
        elf_cal.append(int(cal))
calories.append(elf_cal)

top_three = [0, 0, 0]
for idx, elf_cals in enumerate(calories):
    sum_elf_cals = sum(elf_cals)
    min_top_three = min(top_three)
    min_idx = top_three.index(min_top_three)
    if sum_elf_cals > min_top_three:
        top_three[min_idx] = sum_elf_cals

print(sum(top_three))