# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# 
# Evaluate the sum of all the amicable numbers under 10000.

n0 = 220
n1 = 284

def sum_of_proper_divisors(n):
    return sum([x for x in range(1, n) if n % x == 0])

def is_amicable(a):
    b = sum_of_proper_divisors(a)
    c = sum_of_proper_divisors(b)
    return a == c and a != b

# 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110
n0p = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
n1p = [1, 2, 4, 71, 142]


start = 1
end = 10000
amicables = [x for x in range(start,end) if is_amicable(x)] 

value = sum(amicables)
print(value)
