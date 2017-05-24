# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# BRUTE FORCE SOLUTION RUNS SORT OF SLOW

UPPER_LIMIT = 800
list = (0..UPPER_LIMIT)

result = 0

(0..UPPER_LIMIT).each do |a|
  (a..UPPER_LIMIT).each do |b|
    (b..UPPER_LIMIT).each do |c|
      if a ** 2 + b ** 2 == c ** 2
        if a + b + c == 1000
          result = a * b * c
          break
        end
      end
    end
  end
end

puts result
