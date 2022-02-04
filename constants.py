DEPTH = 1

COORDS_X = [12 + 60 * i for i in range(2, 15)]
COORDS_Y = [12 + 60 * i for i in range(13)]
COORDS = []
for x in COORDS_X:
    for y in COORDS_Y:
        COORDS.append((x, y))

GARBAGE = ['стекло1', 'пластик1', 'бумага']
