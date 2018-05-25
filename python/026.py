# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def is_prime(n):
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3,n):
        if n % i == 0:
            return False
    return True

def detect_cycle(n):
    d0, m0 = divmod(1,n)
    d1, m1 = divmod(10 * m0, n)
    count = 1
    while m0 != m1 and m1 != 1:
        d0, m0 = d1, m1
        d1, m1 = divmod(10 * m0, n)
        count += 1
    return count

start = 1
end = 11
end = 1000

ns = [(x, detect_cycle(x)) for x in range(start,end) if is_prime(x)]

value = max(ns, key=lambda a: a[1])[1]
print(value)
