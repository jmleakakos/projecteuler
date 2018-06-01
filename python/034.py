# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def is_curious(n):
    return n == sum([factorial(int(n)) for n in str(n)])

start = 3
end = 146
end = 50000

curious_numbers = [n for n in range(start,end) if is_curious(n)]

value = sum(curious_numbers)
print(value)
