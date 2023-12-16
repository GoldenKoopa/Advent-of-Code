def print_matrix(matrix):
    print()
    for row in matrix:
        print("".join([str(x) for x in row]))
    print()

def pad_matrix(matrix, padding, depth):
    new_matrix = [row[:] for row in matrix]
    for _ in range(depth):
        new_matrix.insert(0, [padding]*len(new_matrix[0]))
        new_matrix.append([padding]*len(new_matrix[0]))
        
    for i in range(len(new_matrix)):
        new_matrix[i] = [padding]*depth + new_matrix[i] + [padding]*depth
    
    return new_matrix

