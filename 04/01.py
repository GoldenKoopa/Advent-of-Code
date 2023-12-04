import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().split('\n')


# contents = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')


def get_points(winning_numbers, numbers):
    occ = 0
    for elem in numbers:
        if elem in winning_numbers:
            occ += 1
    if occ == 0: return 0
    return 2**(occ-1)


points = 0
for elem in contents:
    winning_numbers = elem.split(": ")[1].split('| ')[0].split()
    numbers = elem.split(": ")[1].split('| ')[1].split()
    print(numbers)
    points += get_points(winning_numbers, numbers)

print(points)