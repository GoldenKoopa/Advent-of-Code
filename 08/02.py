import re
import math

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
current_active_nodes = [elem for elem in list(nodes.keys()) if elem[2] == 'A']
past_nodes = [[] for _ in range(len(current_active_nodes))]



periods = []
for elem in current_active_nodes:
    steps = 0
    false = True
    while false:
        elem = nodes[elem][int(instruction[steps%n])]
        steps += 1
        if elem[2] == 'Z':
            periods.append(steps)
            false = False
print(periods)
print(math.lcm(*periods))
