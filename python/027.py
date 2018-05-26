# Euler discovered the remarkable quadratic formula:
# 
# n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.
# 
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
# 
# n^2+an+b, where |a|<1000 and |b|≤1000
# 
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from math import ceil,sqrt

def is_prime(n):
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, ceil(sqrt(n))+2, 2):
        if n % i == 0:
            return False
    return True

def f1(n):
    return n ** 2 + n + 41

def f2(n):
    return n ** 2 - 79 * n + 1601

def fn(n, a, b):
    return n ** 2 + a * n + b

# start = 0
# end = 40
# print(all([is_prime(f1(x)) for x in range(0,end)]))
# 
# end = 80
# print(all([is_prime(f2(x)) for x in range(0,end)]))

# (a,b) in -1000 < a < 1000 and -1000 < b < 1000
# find a*b when f(n) produces the maximum number of primes
#   for consecutive values of n, starting with n = 0

coefficients = [(-80,1601),(-79,1601)]
coefficients = [(a,b) for a in range(-1000,1000) for b in range(-1000,1000)]


max_number_of_primes = 0
max_product_coefficient = 0
for (a,b) in coefficients:
    n = 0
    cont = True
    while cont:
        v = fn(n,a,b)
        if v > 0 and is_prime(v):
            n += 1
            cont = True
        else:
            cont = False
            if n > max_number_of_primes:
                max_number_of_primes = n
                max_product_coefficient = a * b
            n = 0


value = max_product_coefficient
print(value)
