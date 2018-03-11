from math import ceil

x = y = 0   # coordinates in grid
needle = int(input())
N = 1       # square number
i = 1       # "operation" number, for each direction the spiral goes

# "Go through" the spiral, counting up to the needle
# (the square number we're given), in order to find
# its coordinates, and from there the Manhattan distance
# to the center
# The spiral goes 1 right, 1 up, 2 left, 2 down, 3 right...
# naive O(n) solution
cond = True
while cond:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    movement = directions[(i-1) % 4]
    amount = ceil(i/2)
    #print(amount, ['right', 'up', 'left', 'down'][(i-1)%4])
    i += 1
    
    for _ in range(0, amount):
        if N == needle:
            cond = False
            print(x, y, abs(x)+abs(y))
            break
        x += movement[0]
        y += movement[1]
        N += 1
        #print(x, y, N)
