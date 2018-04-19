# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import numpy

def is_prime(n):
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    limit = int(n ** (.5)) + 1
    for i in range(3,limit,2):
        if n % i == 0:
            return False
    return True

def primes_up_to(n):
    primes = [2]
    if n == 2:
        return primes
    primes.extend([x for x in range(3,n,2) if is_prime(x)])
    return primes

def prime_factors(n):
    primes = primes_up_to(n)
    factors = list(filter(lambda x: n % x == 0, primes))
    return factors


number = 600851475143

value = prime_factors(number)[-1]
print(value)
print(value == 6857)
