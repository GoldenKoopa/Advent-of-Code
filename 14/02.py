import sys
sys.path.append('.')
from utils import print_matrix
from copy import deepcopy

rock_field = [[elem2 for elem2 in elem] for elem in open('14/input.txt').read().splitlines()]\
    

def move_rock(matrix, i, j):
    if matrix[i][j] == 'O' and matrix[i-1][j] == '.':
        matrix[i][j] = '.'
        matrix[i-1][j] = 'O'
        if i != 1:
            move_rock(matrix, i-1, j)

def evaluate_total_load(matrix):
    return sum([matrix[i].count('O') * (len(matrix)-i) for i in range(len(matrix))])


def dont_know_how_to_exit_this_mess():
    final_field = fields[((1000000000-first_field)%(phase))+first_field-1]
    print(phase, first_field)
    # print_matrix(fields[first_field])
    # print_matrix(rock_field)
    # print_matrix(fields[6])
    print(evaluate_total_load(final_field))
    
    exit()


fields = []
for cycle in range(100000000):
    for direction in range(4):
        for i in range(1, len(rock_field)):
            for j in range(len(rock_field[i])):
                move_rock(rock_field, i, j)
        rock_field = list(list(x)[::-1] for x in zip(*rock_field))

        if direction == 3:
            fields.append(deepcopy(rock_field))
            if cycle > 2:
                if fields.count(fields[-1]) == 2:
                    first_field = fields.index(fields[-1])
                    phase = cycle - first_field 
                    dont_know_how_to_exit_this_mess()
            

print_matrix(rock_field)
