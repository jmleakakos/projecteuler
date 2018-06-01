# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# 
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# xy / yz = x / z, y,z != 0

from decimal import *
from fractions import Fraction

def formatted(x,y,z):
    x_s = str(x)
    y_s = str(y)
    z_s = str(z)
    return x_s + y_s + ' / ' + y_s + z_s + ' = ' + x_s + ' / ' + z_s

def equalized(x,y,z):
    top = int(str(x) + str(y))
    bottom = int(str(y) + str(z))
    result = x / z
    return top / bottom == result

x_range = range(0,10)
y_range = range(1,10)
z_range = range(1,10)

numbers = [(Decimal(x) / Decimal(z)) for x in x_range for y in y_range for z in z_range if equalized(x,y,z) if (int(str(x) + str(y)) < int(str(y) + str(z)))]

n = Fraction(numbers[0] * numbers[1] * numbers[2] * numbers[3])

value = n.denominator
print(value)
