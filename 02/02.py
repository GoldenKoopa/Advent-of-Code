import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().split('\n')



sum = 0
for elem in contents:
    max_colors = {'red': [], 'blue': [], 'green': []}
    test = elem.split(':')[1].split(';')
    for substring in test:
        test2 = substring.split(',')
        for subsubstring in test2:
            test3 = subsubstring.split(' ')
            max_colors[test3[2]].append(int(test3[1]))
    sum += max(max_colors['red']) * max(max_colors['green']) * max(max_colors['blue'])



print(sum)