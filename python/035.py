# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

from math import ceil,sqrt

def rotations(n):
    digits = str(n)
    end = len(digits)
    output = []
    for i in range(0,end):
        output.append(int(digits[i:] + digits[:i]))
    return output

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(ceil(sqrt(n))+2), 2):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    rs = rotations(n)
    return all(is_prime(r) for r in rs)

start = 1
end = 1000000

primes = [2,3] + [x for x in range(5,end) if is_prime(x)]
circulars = [n for n in primes if is_circular_prime(n)]

value = len(circulars)
print(value)
