import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().splitlines()


empty_lines = []
empty_columns = []
for i in range(len(contents)):
    if '#' not in contents[i]:
        empty_lines.append(i)

for i in range(len(contents[0])):
    for j in range(len(contents)):
        if contents[j][i] == '#':
            break
    else: empty_columns.append(i)

galaxies = []
for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == '#':
            galaxies.append((j, i))

total = 0
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        x = range(min([galaxies[i][0], galaxies[j][0]]), max([galaxies[i][0], galaxies[j][0]]))
        y = range(min([galaxies[i][1], galaxies[j][1]]), max([galaxies[i][1], galaxies[j][1]]))
        total += len(x) + len(y) 
        for elem in empty_columns:
            if elem in x:
                total += 999999
        for elem in empty_lines:
            if elem in y:
                total += 999999

print(total)