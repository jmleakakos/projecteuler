-- Number letter counts
-- Problem 17 
-- If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
-- 
-- If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
-- 
-- 
-- NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import Data.Char (digitToInt, intToDigit)

main = print $ length $ filter (/=' ') $ concat $ map numberToName [1..1000]

numberToName number
  | len == 1 = numberToNameComponent d
  | len == 2 && d == 1 = numberToNameComponent (10 + head ds)
  | len == 2 = numberToNameComponent (10 * d) ++ " " ++ numberToNameComponent (head ds)
  | len == 3 && all (==0) ds = numberToNameComponent d ++ " hundred" 
  | len == 3 = numberToName (d * 100) ++ " and " ++ numberToName (read $ map intToDigit ds)
  | len == 4 = "one thousand"
  | otherwise = "FULL NUMBER ERROR" 
  where digits@(d:ds) = map digitToInt $ show number
        len = length digits

numberToNameComponent :: Int -> String
numberToNameComponent number 
  | number == 0 = ""
  | number == 1 = "one"
  | number == 2 = "two"
  | number == 3 = "three"
  | number == 4 = "four"
  | number == 5 = "five"
  | number == 6 = "six"
  | number == 7 = "seven"
  | number == 8 = "eight"
  | number == 9 = "nine"
  | number == 10 = "ten"
  | number == 11 = "eleven"
  | number == 12 = "twelve"
  | number == 13 = "thirteen"
  | number == 14 = "fourteen"
  | number == 15 = "fifteen"
  | number == 16 = "sixteen"
  | number == 17 = "seventeen"
  | number == 18 = "eighteen"
  | number == 19 = "nineteen"
  | number == 20 = "twenty"
  | number == 30 = "thirty"
  | number == 40 = "forty"
  | number == 50 = "fifty"
  | number == 60 = "sixty"
  | number == 70 = "seventy"
  | number == 80 = "eighty"
  | number == 90 = "ninety"
  | otherwise = "BASCI NUMBER ERROR " ++ (show number)