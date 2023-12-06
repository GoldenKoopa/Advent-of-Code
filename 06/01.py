contents = '''Time:        53     91     67     68
Distance:   250   1330   1081   1025'''.splitlines()

times = contents[0].split(':')[1].split()
distances = contents[1].split(':')[1].split()

races = [(int(times[i]), int(distances[i])) for i in range(len(times))]

sums = 1
for elem in races:
    for i in range(elem[0]//2):
        if i*(elem[0]-i) > elem[1]:
            sums *= elem[0]-2*i+1
            break
print(sums)
