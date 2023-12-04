import os
import re

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().split('\n')

# contents = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''.split('\n')

def check_surrounding(x):
    print(x)
    x1 = x[0] + 1
    x2 = x[1]
    y = x[2] + 1
    lst = [contents[y+i][x1+j] for i in range(-1, 2) for j in range(-1, 2)]
    lst += [contents[y+i][x2+j] for i in range(-1, 2) for j in range(-1, 2)]
    print(lst)
    if "A" in lst:
        print(True)
        return True
    return False

all_occ = []
for i, elem in enumerate(contents):
    occ = [(m.start(0), m.end(0), i, elem[m.start(0):m.end(0)]) for m in re.finditer(r'\d+', elem)]
    all_occ.append(occ)
    contents[i] = re.sub(r'[*/$#@&=+%-]', 'A', elem)
    contents[i] = '0' + contents[i] + '0'

sum = 0
contents.insert(0, [0]*142)
contents.append([0]*142)


for elem in all_occ:
    for i in range(len(elem)):
        if check_surrounding(elem[i]):
            sum += int(elem[i][3])

print(sum)

