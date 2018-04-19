# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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

def primes(n):
    ps = [2]
    if n == 2:
        return ps
    ps.extend([x for x in range(3,n+1,2) if is_prime(x)])
    return ps

def prime_factor_count(prime, number, count=0):
    div, mod = divmod(number, prime)
    if mod > 0:
        return count
    if div > 1:
        return prime_factor_count(prime, div, count + 1)
    return count + 1

def prime_factors_counts(n):
    factors = filter(lambda x: n % x == 0, primes(n))
    counts = {}
    for factor in factors:
        count = prime_factor_count(factor, n)
        counts[factor] = count

    return counts 

def lcm_up_to(n):
    final_prime_counts = {}
    for v in range(2,n+1):
        pfc = prime_factors_counts(v)
        for prime,count in pfc.items():
            if prime in final_prime_counts:
                if final_prime_counts[prime] < count:
                    final_prime_counts[prime] = count
            else:
                final_prime_counts[prime] = count
    lcm = 1
    for prime,count in final_prime_counts.items():
        lcm = lcm * (prime ** count)
    return lcm 

limit = 20
value = lcm_up_to(limit) 

print(value)
print(value == 232792560)

