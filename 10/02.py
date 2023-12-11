import sys
sys.path.append('.')
from utils import print_matrix, flood_fill

with open('10/input.txt', 'r') as file:
    contents = [list(elem) for elem in file.read().splitlines()]


directions = {'|': 'NS',
              '-': 'EW',
              'L': 'NE',
              'J': 'NW',
              '7': 'SW',
              'F': 'SE'}

coordinate_change = {'N': (0, -1),
                     'S': (0, 1),
                     'E': (1, 0),
                     'W': (-1, 0)}

def get_next_tile(coordinates, direction):
    x = coordinates[0]
    y = coordinates[1]
    direction ='NS'.replace(direction, '') if direction in 'NS' else 'WE'.replace(direction, '')
    next_direction = directions[contents[y][x]].replace(direction, '')
    change = coordinate_change[next_direction]
    return (x + change[0], y + change[1]), next_direction
    
def find_start():
    for y in range(len(contents)):
        if 'S' in contents[y]:
            return (contents[y].index('S'), y)

def find_starting_direction(coordinates):
    x, y = coordinates
    for elem in 'NESW':
        opposite_direction ='NS'.replace(elem, '') if elem in 'NS' else 'WE'.replace(elem, '')
        try:
            get_next_tile((x + coordinate_change[elem][0], y + coordinate_change[elem][1]), elem)
            return elem
        except:
            pass

def rewrite_matrix(matrix, points):
    return [[matrix[y][x] if (x, y) in points else '.' for x in range(len(matrix[0]))] for y in range(len(matrix))]
    
def enlarge_matrix(matrix):
    new_matrix = [[1 if matrix[y//3][x//3] != 'S' else 0 for x in range(len(matrix[0])*3)] for y in range(len(matrix)*3)]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '|':
                new_matrix[y * 3 + 1][x * 3 + 1] = 0
                new_matrix[y * 3][x * 3 + 1] = 0
                new_matrix[y * 3 + 2][x * 3 + 1] = 0
            elif matrix[y][x] == '-':
                new_matrix[y * 3 + 1][x * 3 + 1] = 0
                new_matrix[y * 3 + 1][x * 3 ] = 0
                new_matrix[y * 3 + 1][x * 3 + 2] = 0
            elif matrix[y][x] == 'J':
                new_matrix[y * 3 + 1][x * 3 + 1] = 0
                new_matrix[y * 3 + 1][x * 3] = 0
                new_matrix[y * 3][x * 3 + 1] = 0
            elif matrix[y][x] == '7':
                new_matrix[y * 3 + 1][x * 3 + 1] = 0
                new_matrix[y * 3 + 1][x * 3] = 0
                new_matrix[y * 3 + 2][x * 3 + 1] = 0
            elif matrix[y][x] == 'L':
                new_matrix[y * 3 + 1][x * 3 + 1] = 0
                new_matrix[y * 3 + 1][x * 3 + 2] = 0
                new_matrix[y * 3 ][x * 3 + 1] = 0
            elif matrix[y][x] == 'F':
                new_matrix[y * 3 + 1][x * 3 + 1] = 0
                new_matrix[y * 3 + 1][x * 3 + 2] = 0
                new_matrix[y * 3 + 2][x * 3 + 1] = 0
    return new_matrix
            
        
coordinates = find_start()
direction = find_starting_direction(coordinates)

coordinates = (coordinates[0] + coordinate_change[direction][0], coordinates[1] + coordinate_change[direction][1])
pipe = [coordinates]
while contents[coordinates[1]][coordinates[0]] != 'S':
    coordinates, direction = get_next_tile(coordinates, direction)
    pipe.append(coordinates)

contents = rewrite_matrix(contents, pipe)
enlarged_matrix = enlarge_matrix(contents)
flood_fill(enlarged_matrix, 0, 0, 0, 1)

total = 0
for y in range(len(contents)):
    for x in range(len(contents[0])):
        if enlarged_matrix[y*3 + 1][x*3 + 1]:
            total += 1

print("Total tiles:", total)