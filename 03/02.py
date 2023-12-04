import os
import re

contents = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split('\n')



occ = []
for i, elem in enumerate(contents):
    occ += [(m.start(0), i) for m in re.finditer(r'\*', elem)]
    contents[i] = '0' + contents[i] + '0'

contents.insert(0, [0]*142)
contents.append([0]*142)

def check_surrounding(x):
    x1 = x[0] + 1
    y = x[1] + 1
    lst = [contents[y+i][x1+j] for i in range(-1, 2) for j in range(-1, 2)]
    ind = [int(i) for i in range(len(lst)) if lst[i] in '0123456789']
    for i in range(len(ind)):
        if ind[i] == 3 or ind[i] == 5:
            ind[i] *= 10
    if len(ind) < 2: return
    if max(ind) - min(ind) > 2:
        return
    
    
    print(ind)

check_surrounding(occ[0])
print(occ)