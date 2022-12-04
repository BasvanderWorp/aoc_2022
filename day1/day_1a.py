
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

max_cals = 0
for idx, elf_cals in enumerate(calories):
    max_cals = max(max_cals, sum(elf_cals))

print(max_cals)
