def isValid(matrix, x, y, pattern):
    if x < 0 or x >= len(matrix[0]): return False
    if y < 0 or y >= len(matrix): return False
    if matrix[y][x] not in pattern: return False
    return True

def flood_fill(matrix, x, y, fill, pattern: list):
    if type(pattern) != type([]): pattern = [pattern]
    queue = []
    queue.append((x, y))
    matrix[y][x] = fill
    
    while queue:
        current_pixel = queue.pop()
        posX = current_pixel[0]
        posY = current_pixel[1]
        
        if isValid(matrix, posX+1, posY, pattern):
            matrix[posY][posX+1] = fill
            queue.append((posX+1, posY))
        if isValid(matrix, posX-1, posY, pattern):
            matrix[posY][posX-1] = fill
            queue.append((posX-1, posY))
        if isValid(matrix, posX, posY+1, pattern):
            matrix[posY+1][posX] = fill
            queue.append((posX, posY+1))
        if isValid(matrix, posX, posY-1, pattern):
            matrix[posY-1][posX] = fill
            queue.append((posX, posY-1))