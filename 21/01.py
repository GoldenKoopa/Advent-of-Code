import sys
sys.path.append('.')
from utils import print_matrix, pad_matrix, search_matrix
from copy import deepcopy

contents = [[elem2 for elem2 in elem] for elem in open('21/input.txt').read().splitlines()]

contents = pad_matrix(contents, '#', 1)

n = len(contents[0])
m = len(contents)

current_tiles = search_matrix(contents, 'S')
for step in range(64):
    new_tiles = []
    for x, y in current_tiles:
        if contents[y%m][(x-1)%n] != '#' and (x-1, y) not in new_tiles: new_tiles.append((x-1, y))
        if contents[y%m][(x+1)%n] != '#' and (x+1, y) not in new_tiles: new_tiles.append((x+1, y))
        if contents[(y+1)%m][x%n] != '#' and (x, y+1) not in new_tiles: new_tiles.append((x, y+1))
        if contents[(y-1)%m][x%n] != '#' and (x, y-1) not in new_tiles: new_tiles.append((x, y-1))
    current_tiles = deepcopy(new_tiles)

print(len(current_tiles))
        
        
