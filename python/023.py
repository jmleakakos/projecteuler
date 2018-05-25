# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import itertools

def proper_divisors(n):
    return [x for x in range(1,int(n/2)+1) if n % x == 0]

def is_perfect(n):
    return sum(proper_divisors(n)) == n

def is_deficient(n):
    return sum(proper_divisors(n)) < n

def is_abundant(n):
    return sum(proper_divisors(n)) > n

start = 1
end = 28123

abundant_numbers = [x for x in range(start, end) if is_abundant(x)]

all_abundants_pairs = itertools.product(abundant_numbers, abundant_numbers)
all_abundant_sums = [a + b for (a,b) in all_abundants_pairs if a + b < end]

a = set(all_abundant_sums)

output = []
for i in range(start, end):
    if i not in a:
        output.append(i)

value = sum(output)
print(value)
