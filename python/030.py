# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def sum_of_nth_power_of_digits_of_value(n, v):
    return 

p = 5
start = 2
end = 1000000

f = lambda x: sum([int(a)**p for a in str(x)])

ns = [n for n in range(start,end) if n == f(n)]

value = sum(ns)
print(value)
