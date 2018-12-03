covered = set()
overlap = set()

for line in open('input.txt', 'r'):
    data = line[:-1].split(' ')

    coords = data[3].split('x')
    width = int(coords[0])
    height = int(coords[1])

    start_coords = data[2][:-1].split(',')
    x = int(start_coords[0])
    y = int(start_coords[1])

    for i in range(width):
        for j in range(height):
            spot = (x+i, y+j)

            if spot in covered:
                overlap.add(spot)
            
            covered.add(spot)

print(len(overlap))