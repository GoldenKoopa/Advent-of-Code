import sys
sys.path.append('.')

contents = open('15/input.txt').read().split(',')


def hash_algorithm(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total


print(sum([hash_algorithm(elem) for elem in contents]))