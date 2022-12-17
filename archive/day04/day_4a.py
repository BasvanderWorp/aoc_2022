
with open('input.txt', 'r') as f:
    # lines = f.read().splitlines()
    lines = f.readlines()

no_cr = [line.split('\n')[0] for line in lines]
pairs = [line.split(',') for line in no_cr]

set_pairs = []
for pair in pairs:
    set_pair = []
    spaces_list = []
    for x in range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1])+1):
        spaces_list.append(x)
    set_pair.append(set(spaces_list))
    spaces_list = []
    for x in range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1])+1):
        spaces_list.append(x)
    set_pair.append(set(spaces_list))
    set_pairs.append(set_pair)

overlapping_pairs_count = 0
for pair in set_pairs:
    if pair[0] & pair[1] == pair[0]:
        overlapping_pairs_count += 1
    elif pair[0] & pair[1] == pair[1]:
        overlapping_pairs_count += 1

print(overlapping_pairs_count)

