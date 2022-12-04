def prio(ch):
    if ch.islower():
        return(ord(ch)- ord('a') + 1)
    else:
        return (ord(ch) - ord('A') + 27)

def get_dupl(r1, r2, r3):
    return set(r1) & set(r2) & set(r3)

with open('input.txt', 'r') as f:
    rucksacks = f.read().splitlines()


sum_dupl_items = 0

elf_set = []
for idx, r in enumerate(rucksacks):
    elf_set.append(r)
    if (idx+1) % 3 == 0:
        ch = get_dupl(elf_set[0], elf_set[1], elf_set[2])
        sum_dupl_items += prio(list(ch)[0])
        elf_set = []

print(sum_dupl_items)




