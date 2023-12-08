import re


import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().splitlines()

instruction = contents.pop(0).replace('L', '0').replace('R', '1')
del contents[0]

nodes = {}
for line in contents:
    matches = re.findall(r'[A-Z]{3}', line)
    nodes[matches[0]] = (matches[1], matches[2])

n = len(instruction)
current_node = 'AAA'
steps = 0
false = True # moritz ist schuld
while false:
    current_node = nodes[current_node][int(instruction[steps%n])]
    print(current_node)
    steps += 1
    if current_node == 'ZZZ':
        false = False

print(steps)