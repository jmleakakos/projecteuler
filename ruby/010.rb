# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

require 'prime'

UPPER_LIMIT = 2000000

sum = 0
Prime.each { |prime| prime < UPPER_LIMIT ? sum += prime : break; }
puts sum
