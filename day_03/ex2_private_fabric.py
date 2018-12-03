for line1 in open('input.txt', 'r'):
    data1 = line1[:-1].split(' ')
    coords1 = data1[3].split('x')
    start_coords1 = data1[2][:-1].split(',')

    x1 = int(start_coords1[0])
    y1 = int(start_coords1[1])
    width1 = int(coords1[0])
    height1 = int(coords1[1])

    covered = set()

    print(f'==========> {data1}')

    for i in range(width1):
        for j in range(height1):
            spot = (x1+i, y1+j)
            covered.add(spot)

    for line2 in open('input.txt', 'r'):
        if line1 != line2:
            data2 = line2[:-1].split(' ')
            coords2 = data2[3].split('x')
            start_coords2 = data2[2][:-1].split(',')

            x2 = int(start_coords2[0])
            y2 = int(start_coords2[1])
            width2 = int(coords2[0])
            height2 = int(coords2[1])

            overlap_found = False

            for i in range(width2):
                for j in range(height2):
                    spot = (x2+i, y2+j)

                    if spot in covered:
                        print(f'Uh oh! Line {line1} overlaps with {line2}!')
                        overlap_found = True
                        break
                
                if overlap_found:
                    break
            
            if overlap_found:
                break
    
    if not overlap_found:
        print(f'\n\n\nYay! Line \"{line1}\" overlaps with no other!"')
        break
