# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# for all numbers A x B = C, where A,B from a through b and b > a, check if (ABC) is 1-9 pandigital

def digits(n):
    return [int(x) for x in str(n)]

def is_one_through_nine_pandigital(n):
    one_through_nine = digits(123456789)
    n_digits = digits(n)
    
    one_through_nine.sort()
    n_digits.sort()

    return one_through_nine == n_digits

def concat_numbers(a,b,c):
    return str(a) + str(b) + str(c)

start = 1
end = 2000

number_range = range(start, end+1)

output = sum(set([a*b for a in number_range for b in number_range if is_one_through_nine_pandigital(concat_numbers(a,b,a*b))]))
print(output)


value = 0
print(value)
