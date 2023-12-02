import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('01.txt', 'r') as file:
    contents = file.read().split('\n')

def find_numbers(string):
    numbers = [num for num in string if num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
    return int(f'{numbers[0]}{numbers[-1]}')

sum = 0
for elem in contents:
    sum += find_numbers(elem)
print(sum)
