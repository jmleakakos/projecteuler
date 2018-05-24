# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

import math

size = 2
size = 20

# combination n!/((n-r)!(r)!)
# 4 total symbols, 2 downs, 2 rights
# size + 1 total symbols, size - 1 downs, size -1 rights

total_symbols = size + size
downs = size
rights = total_symbols - downs


total = math.factorial(total_symbols)
subset = math.factorial(downs) * math.factorial(rights)

value = total / subset
print(value)
print(value == 137846528820)


size = 2
size = 20

grid = [[0,0,0],[0,0,0],[0,0,0]]
grid = [[0]*(size+1) for i in range(size+1)]

for i in range(size+1):
    grid[i][size] = 1
    grid[size][i] = 1

for i in reversed(range(size)):
    for j in reversed(range(size)):
        grid[i][j] = grid[i+1][j] + grid[i][j+1]

value = grid[0][0]
print(value)
print(value == 137846528820)
