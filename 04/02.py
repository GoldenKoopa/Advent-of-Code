import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().split('\n')

def get_points(winning_numbers, numbers):
    occ = 0
    for elem in numbers:
        if elem in winning_numbers:
            occ += 1
    if occ == 0: return [0, 0, 1]
    return [2**(occ-1), occ, 1]

points = []
for elem in contents:
    winning_numbers = elem.split(": ")[1].split('| ')[0].split()
    numbers = elem.split(": ")[1].split('| ')[1].split()
    points.append(get_points(winning_numbers, numbers))

for i, elem in enumerate(points):
    for j in range(i + 1, i + elem[1] + 1):
        points[j][2] += elem[2]

end_points = sum([elem[2] for elem in points])
print(end_points) #8570000