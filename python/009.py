# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

r = range(1, 500)

s = [a*b*c for a in r for b in range(a+1, 500) for c in range(b+1, 500) if a+b+c == 1000 and a*a+b*b == c*c]

value = s[0]
print(value)
print(value == 31875000)
