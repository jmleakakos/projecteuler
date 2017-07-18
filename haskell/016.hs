-- Power digit sum
-- Problem 16 
-- 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
-- 
-- What is the sum of the digits of the number 21000?

import Data.Char (digitToInt)


main = print $ sumOfDigits (2 ** 1000)

sumOfDigits num = sum $ map digitToInt $ show $ floor num