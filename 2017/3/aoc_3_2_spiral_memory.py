from math import ceil
from itertools import product

x = y = 0   # coordinates in grid
needle = int(input())
N = 1       # square number
i = 1       # "operation" number, for each direction the spiral goes
spiral = {(0, 0): 1}

# Function to determine the value of a new square in the spiral.
# Each square is the sum of the squares around it, that are before it.
# Each square can have up to 5 neighbors, but this just tries to find
# neighbors in all 8 positions around it. This should always find no more
# than 5 neighbors while building the spiral
def sumSurround(x, y):
    neighborsRel = [v for v in product([-1, 0, 1], repeat=2)
                    if v != (0, 0)]
    neighbors = [(n[0]+x, n[1]+y) for n in neighborsRel]

    s = 0
    for n in neighbors:
        s += spiral.get(n, 0)
    return s
    

# Populate the spiral. When a square with a value larger than needle is
# found, return it.
# The spiral goes 1 right, 1 up, 2 left, 2 down, 3 right...
finding = True
while finding:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    movement = directions[(i-1) % 4]
    amount = ceil(i/2)
    #print(amount, ['right', 'up', 'left', 'down'][(i-1)%4])
    i += 1
    
    for _ in range(0, amount):
        if spiral[(x, y)] > needle:
            finding = False
            print(f'value={spiral[(x,y)]} at ({x}, {y})')
            break
        N += 1
        x += movement[0]
        y += movement[1]
        spiral[(x, y)] = sumSurround(x, y)
        #print(x, y, N)
