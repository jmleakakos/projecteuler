# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from math import ceil,sqrt

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, ceil(sqrt(n))+2, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    a = str(n)
    if is_prime(n):
        ltr_strings = [a[x:] for x in range(1,len(a))]
        rtl_strings = [a[0:x] for x in range(1,len(a))[::-1]]
        ltr = all([is_prime(int(a[x:])) for x in range(1,len(a))])
        rtl = all([is_prime(int(a[0:x])) for x in range(1,len(a))[::-1]])
        if ltr and rtl:
            return True
    return False

i = 11
c = 0
truncatable_primes = []

while c < 11:
    if is_truncatable_prime(i):
        truncatable_primes.append(i)
        c += 1
    i += 2

value = sum(truncatable_primes)
print(value)
