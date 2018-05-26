# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# 
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


# 1+0 - 1
# 3+2 - 3 5 7 9
# 5+4 - 13 17 21 25
# 7+6 - 31 37 43 49

def sum_of_diagonals_for_size(n):
    c = 1
    s = 1
    if n == 1:
        return s
    counter = 2
    for i in range(3,n+1,2):
        c1 = c + counter
        c2 = c1 + counter
        c3 = c2 + counter
        c4 = c3 + counter
        c = c4
        s = s + c1 + c2 + c3 + c4
        counter += 2
    return s

print(sum_of_diagonals_for_size(5))

limit = 1001
value = sum_of_diagonals_for_size(limit)
print(value)
