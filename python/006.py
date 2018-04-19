# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 100

numbers = range(1, limit + 1)
sum_of_squares = sum([x*x for x in numbers])
square_of_sums = sum(numbers) * sum(numbers)

value = square_of_sums - sum_of_squares
print(value)
print(value == 25164150)
