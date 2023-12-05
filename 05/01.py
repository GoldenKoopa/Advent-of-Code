import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open('input.txt', 'r') as file:
    contents = file.read().split('\n\n')



# contents = '''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''.split('\n\n')
# print(contents)

seeds = contents[0].split(':')[1].split()
seed_to_soil = [elem.split() for elem in contents[1].split(':\n')[1].splitlines()]
soil_to_fertilizer = [elem.split() for elem in contents[2].split(':\n')[1].splitlines()]
fertilizer_to_water = [elem.split() for elem in contents[3].split(':\n')[1].splitlines()]
water_to_light = [elem.split() for elem in contents[4].split(':\n')[1].splitlines()]
light_to_temp = [elem.split() for elem in contents[5].split(':\n')[1].splitlines()]
temp_to_humi = [elem.split() for elem in contents[6].split(':\n')[1].splitlines()]
humi_to_loc = [elem.split() for elem in contents[7].split(':\n')[1].splitlines()]

for elem in seed_to_soil: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))
for elem in soil_to_fertilizer: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))
for elem in fertilizer_to_water: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))
for elem in water_to_light: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))
for elem in light_to_temp: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))
for elem in temp_to_humi: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))
for elem in humi_to_loc: elem.append(range(int(elem[1]), int(elem[1])+int(elem[2])))



locs = []
for seed in seeds:
    for elem in seed_to_soil:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    for elem in soil_to_fertilizer:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    for elem in fertilizer_to_water:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    for elem in water_to_light:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    for elem in light_to_temp:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    for elem in temp_to_humi:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    for elem in humi_to_loc:
        if int(seed) in elem[3]:
            seed = int(seed) - int(elem[1]) + int(elem[0])
            break
    locs.append(seed)

print(min(locs))
    