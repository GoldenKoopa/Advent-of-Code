import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().splitlines()

def get_delta_y(lst):
    delta_y = []
    for i in range(1, len(lst)):
        delta_y.append(lst[i] - lst[i-1])
    if len(set(delta_y)) == 1:
        return delta_y[0]
    else: return delta_y[-1] + get_delta_y(delta_y) #delta_y[0] - get_delta_y(delta_y) for part 2
        
extrapolated_values = []
for elem in contents:
    lst = [int(val) for val in elem.split()]
    extrapolated_values.append(lst[-1] + get_delta_y(lst)) #see last comment

print(sum(extrapolated_values))