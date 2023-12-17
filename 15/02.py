import sys
sys.path.append('.')

contents = open('15/input.txt').read().split(',')


def hash_algorithm(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total


boxes = {i: [] for i in range(256)}
for lens in contents:
    if '-' in lens:
        box = hash_algorithm(lens[:-1])
        lenses = [elem[0] for elem in boxes[box]]
        if lens[:-1] in lenses:
            del boxes[box][lenses.index(lens[:-1])]
        
    else:
        box = hash_algorithm(lens[:-2])
        lenses = [elem[0] for elem in boxes[box]]
        if lens[:-2] in lenses:
            boxes[box][lenses.index(lens[:-2])][1] = int(lens[-1])
        else:
            boxes[box].append([lens[:-2], int(lens[-1])])
            

total = 0 
for i in range(256):
    for j in range(len(boxes[i])):
        total += (i+1)*(j+1)*boxes[i][j][1]
        
print(total)