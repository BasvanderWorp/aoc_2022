import sys
from collections import deque
from helpers.io import read_input

test = False
#test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

L = [line.strip() for line in file_lines]
G = [[44]*(len(L[0]) + 2)] + [[44] + [ord(c) - ord('a') if c.islower() else c for c in line] + [44] for line in L] + [[44]*(len(L[0]) + 2)]

for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] == 'S': start, G[i][j] = (i, j), 0
        if G[i][j] == 'E': end, G[i][j] = (i, j), 25

seen, Q = set(), deque([(0, start)])
while len(Q):
    dist, curr = Q.popleft()
    if curr in seen: continue
    seen.add(curr)
    if curr == end:
        print(dist)
        break
    for dr in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_point = tuple(sum(x) for x in zip(curr, dr))
        if G[curr[0]][curr[1]] + 1 >= G[next_point[0]][next_point[1]]: Q.append((dist + 1, next_point))
        # To put it differently:
        # G(next_point) <= G(curr) + 1
        # hmm that is strange? so G(next_point) could be 2 or more smaller than G(curr) and that would be okay?
        # lets debug this at (1,4)

