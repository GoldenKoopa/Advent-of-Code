import sys
sys.path.append('.')
from utils import print_matrix

rock_field = [[elem2 for elem2 in elem] for elem in open('14/input.txt').read().splitlines()]\
    
print_matrix(rock_field)

def move_rock(matrix, i, j):
    if matrix[i][j] == 'O' and matrix[i-1][j] == '.':
        matrix[i][j] = '.'
        matrix[i-1][j] = 'O'
        if i != 1:
            move_rock(matrix, i-1, j)

def evaluate_total_load(matrix):
    return sum([matrix[i].count('O') * (len(matrix)-i) for i in range(len(matrix))])

for i in range(1, len(rock_field)):
    for j in range(len(rock_field[i])):
        move_rock(rock_field, i, j)

print_matrix(rock_field)
print(evaluate_total_load(rock_field))