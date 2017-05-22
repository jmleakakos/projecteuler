# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# for all multiples of 20, check if the other numbers are also a mutliple

require 'prime'

primeDivisions = (2..20).map do |n|
  Prime::prime_division(n)
end

lcmMap = {}

primeDivisions.each do |primeCount|
  primeCount.each do |prime, count|
    if (lcmMap[prime] != nil && lcmMap[prime] < count) || (lcmMap[prime] == nil)
      lcmMap[prime] = count
    end
  end
end
lcm = lcmMap.inject(1) do |acc, primeCount|
  prime = primeCount[0]
  count = primeCount[1]
  acc * prime ** count
end
puts lcm
