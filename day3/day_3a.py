def prio(ch):
    if ch.islower():
        return(ord(ch)- ord('a') + 1)
    else:
        return (ord(ch) - ord('A') + 27)

with open('input.txt', 'r') as f:
    rucksacks = f.read().splitlines()


sum_dupl_items = 0

for r in rucksacks:
    left_c = r[:int(len(r)/2)]
    right_c = r[int(len(r)/2):]
    dupl = set(left_c).intersection(set(right_c))
    dupl_ch = list(dupl)[0]
    prio_ch = prio(dupl_ch)
    sum_dupl_items += prio_ch
    print(dupl_ch, prio(dupl_ch), sum_dupl_items)


print(sum_dupl_items)




