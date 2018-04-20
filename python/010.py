# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

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

limit = 2000000
value = sum(primes_up_to(limit))
print(value)
print(value == 142913828922)
