import sys
sys.path.append('.')

contents = [elem for elem in open('13/input.txt').read().split('\n\n')]

def check_horizontal(pattern):
    for i in range(1, len(pattern)):
        is_mirror = True
        for j in range(min(i, len(pattern)-i)):
            if pattern[i-j-1] != pattern[i+j]:
                is_mirror = False
        if is_mirror: return i
    return 0

def check_vertical(pattern):
    inverted_pattern = []
    for i in range(len(pattern[0])):
        row = ''.join([line[i] for line in pattern])
        inverted_pattern.append(row)
    return check_horizontal(inverted_pattern)

total = 0
for pattern in contents:
    pattern = pattern.splitlines()
    total += check_horizontal(pattern) *100
    total += check_vertical(pattern)
    
print(total)