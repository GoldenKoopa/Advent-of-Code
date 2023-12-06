
contents = '''Time:        53     91     67     68
Distance:   250   1330   1081   1025'''.splitlines()

time = int(contents[0].split(':')[1].strip().replace(' ', ''))
distance = int(contents[1].split(':')[1].strip().replace(' ', ''))

print(time - 2*int(time/2 - ((time/2)**2-distance)**(1/2)+1)+1)