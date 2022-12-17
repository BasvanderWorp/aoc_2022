from helpers.io import read_input

calories = read_input('input_test   .txt', dtype='int', sublists_on_newline=True)

top_three = [0, 0, 0]
for idx, elf_cals in enumerate(calories):
    sum_elf_cals = sum(elf_cals)
    min_top_three = min(top_three)
    min_idx = top_three.index(min_top_three)
    if sum_elf_cals > min_top_three:
        top_three[min_idx] = sum_elf_cals

print(sum(top_three))