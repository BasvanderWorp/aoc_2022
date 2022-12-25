"""
Advent of Code 2022
Day 12, b

"""
from helpers.io import read_input
import heapq
from math import inf
import numpy as np

def neighbours(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
def climb(start, end, heightmap):
    queue = []
    visited = {start}
    path_len = 0
    while start != end:
        for q in neighbours(*start):
            dist = heightmap[start] - heightmap[q]
            if dist >= -1 and q not in visited:
                visited.add(q)
                heapq.heappush(queue, (dist, path_len + 1, q))
        if not queue:
            return inf
        _, path_len, start = heapq.heappop(queue)
    return path_len

# ======================================
# MAIN
# ======================================

test = False
#test = True
input_file = 'input.txt' if not test else 'input_test.txt'
file_lines = read_input(input_file)

# Aanpak
# met heapq een binaire boom bouwen, maar nu de
# Stap 1 : eerst zelf de heapq oplossing nabouwen: OK

# Eerst S en E achterhalen
# dictionary van tuples met heights
# maar nu met een numpy array, vind ik mooier: OK

# nu opdracht 2:
# Wow hoe los ik dit nu op:
# 1) zoek alle a's en draai het algo van opdracht 1. hmm dat werkt niet

L= [line.strip() for line in file_lines]
G = [[44] * (len(L[0]) + 2)] + \
    [[44] + [ord(c) - ord('a') if c.islower() else c for c in line] + [44] for line in L] + \
    [[44] * (len(L[0]) + 2)]

starting_points = []
for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] == 'S':
            start, G[i][j] = (i, j), 0
        if G[i][j] == 0:
            starting_points.append((i,j))
        if G[i][j] == 'E':
            end, G[i][j] = (i, j), 25
heightmap = np.array(G)


shortest_path = inf
for start in starting_points:
    shortest_path = min(shortest_path, climb(start, end, heightmap))

print(shortest_path)
