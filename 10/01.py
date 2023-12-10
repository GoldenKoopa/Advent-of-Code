import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().splitlines()

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


        
coordinates = find_start()
direction = find_starting_direction(coordinates)

coordinates = (coordinates[0] + coordinate_change[direction][0], coordinates[1] + coordinate_change[direction][1])
steps = 1
while contents[coordinates[1]][coordinates[0]] != 'S':
    coordinates, direction = get_next_tile(coordinates, direction)
    steps += 1
print(steps//2)