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

for i in range(len(empty_lines)):
    contents.insert(empty_lines[i], '.'*len(contents[0]))
    empty_lines = [elem+1 for elem in empty_lines]

for i in range(len(empty_columns)):
    for j in range(len(contents)):
        contents[j] = contents[j][:empty_columns[i]] + '.' + contents[j][empty_columns[i]:]
    empty_columns = [elem+1 for elem in empty_columns]

galaxies = []
for i in range(len(contents)):
    for j in range(len(contents[i])):
        if contents[i][j] == '#':
            galaxies.append((j, i))

total = 0
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(total)