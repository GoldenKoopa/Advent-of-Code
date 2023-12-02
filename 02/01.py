import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().split('\n')


max_colors = {'red': 12, 'blue': 14, 'green': 13}
sum = 0
for elem in contents:
    valid = True
    test = elem.split(':')[1].split(';')
    for substring in test:
        test2 = substring.split(',')
        for subsubstring in test2:
            test3 = subsubstring.split(' ')
            if max_colors[test3[2]] < int(test3[1]):
                valid = False

    if valid:
        sum += int(elem.split(':')[0].split(' ')[1])

print(sum)

