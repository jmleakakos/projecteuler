-- Largest prime factor
-- Problem 3 
-- The prime factors of 13195 are 5, 7, 13 and 29.
-- 
-- What is the largest prime factor of the number 600851475143 ?

import Data.List

isPrime :: Int -> Bool
isPrime 1 = False
isPrime 2 = True
isPrime 3 = True
isPrime n 
  | n `mod` 2 == 0 = False
  | otherwise      = not $ any (\x -> n `mod` x == 0) [x | x <- [3..upperLimit], odd x]
  where upperLimit = floor $ sqrt (fromIntegral n)

primes = 2 : [x | x <- [3..], odd x, isPrime x]

main = print $ find (\x -> v `mod` x == 0) ps
  where ps = reverse $ takeWhile (< (floor $ sqrt (fromIntegral v))) primes
        v = 600851475143
