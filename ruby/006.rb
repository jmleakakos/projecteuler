# Sum square difference
# Problem 6 
# The sum of the squares of the first ten natural numbers is,
# 
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sumOfSquares(n)
  (1..n).inject(0) { |acc, v| acc + v ** 2 }
end 

def squareOfSum(n)
  (1..n).inject(0) { |acc, v| acc + v } ** 2
end

def runFor(n)
  squareOfSum(n) - sumOfSquares(n)
end

puts runFor(100)
