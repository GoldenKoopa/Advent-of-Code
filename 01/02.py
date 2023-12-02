import os
import regex as re

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('01.txt', 'r') as file:
    contents = file.read().split('\n')



numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sum = 0
for elem in contents:
    occ = re.findall('[0-9]|one|two|three|four|five|six|seven|eight|nine|zero', elem, overlapped=True)
    print(occ)
    x1 = int(occ[0]) if occ[0] not in numbers else numbers.index(occ[0])
    x2 = int(occ[-1]) if occ[-1] not in numbers else numbers.index(occ[-1])
    print(x1, x2)
    sum += 10*x1 + x2
print(sum)