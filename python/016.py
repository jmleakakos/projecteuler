# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# 
# What is the sum of the digits of the number 2^1000?

def digits(n):
    return [int(x) for x in str(n)]

def sum_of_digits(n):
    return sum(digits(n))

n = 2 ** 15
n = 2 ** 1000

value = sum_of_digits(n)
print(value)
print(value == 1366)
