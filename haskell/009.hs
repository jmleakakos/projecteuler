-- Special Pythagorean triplet
-- Problem 9 
-- A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
-- 
-- a2 + b2 = c2
-- For example, 32 + 42 = 9 + 16 = 25 = 52.
-- 
-- There exists exactly one Pythagorean triplet for which a + b + c = 1000.
-- Find the product abc.

isPythagoreanTriplet a b c = a * a + b * b == c * c

limit = 800

main = (print . head) [a * b * c | a <- [1..limit], b <- [a..limit], c <- [b..limit], isPythagoreanTriplet a b c, a + b + c == 1000]
