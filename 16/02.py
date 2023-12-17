import sys
sys.path.append('.')
from utils import print_matrix, pad_matrix

contents = [[elem2 for elem2 in elem] for elem in open('16/input.txt').read().splitlines()]

print_matrix(contents)

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


connections = {
    "|": [(NORTH, SOUTH)],
    "-": [(WEST, EAST)],
    "/": [(SOUTH, EAST),
          (NORTH, WEST)],
    "\\": [(SOUTH, WEST),
           (NORTH, EAST)]
}

opposite = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}


# print_matrix(visited_squares)
# print_matrix(visited_squares_directions)

def evaluate_energized_tiles(matrix):
    return sum([line.count('#') for line in matrix])

starting_points = []
for i in range(1, len(contents)-1):
    starting_points.append((1, i, EAST))
    starting_points.append((len(contents[0]), i, WEST))

for i in range(1, len(contents[0])-1):
    starting_points.append((i, 1, SOUTH))
    starting_points.append((i, len(contents), NORTH))

print(starting_points)

total = 0
for elem in starting_points:
    matrix = pad_matrix(contents, 0, 1)
    visited_squares = [['.']*len(matrix[0]) for _ in range(len(matrix))]
    visited_squares_directions = [[[] for __ in range(len(matrix[0]))]  for _ in range(len(matrix))]
    queue = [elem]
    while queue:
        x, y, direction = queue.pop(0)
        if matrix[y][x] == 0: continue
        if visited_squares[y][x] != '.' and direction in visited_squares_directions[y][x]:
            continue
        if matrix[y][x] == '.':
            queue.append((x+direction[0], y+direction[1], direction))
        else:
            new_possible_directions = connections[matrix[y][x]]
            if len(new_possible_directions) == 1:
                if direction in new_possible_directions[0]:
                    queue.append((x+direction[0], y+direction[1], direction))
                else:
                    for elem in new_possible_directions[0]:
                        queue.append((x + elem[0], y + elem[1], elem))
            else:
                for elem in new_possible_directions:
                    if opposite[direction] in elem:
                        new_direction = elem[(elem.index(opposite[direction])+1)%2]
                        queue.append((x + new_direction[0], y + new_direction[1], new_direction))
            
        
        visited_squares[y][x] = '#'
        visited_squares_directions[y][x].append(direction)

    total = max(total, evaluate_energized_tiles(visited_squares))
    
print(total)
