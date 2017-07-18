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
  | otherwise = "ERROR " ++ (show number)
  where digits@(d:ds) = map digitToInt $ show number
        len = length digits

numberToNameComponent :: Int -> String
numberToNameComponent 0 = ""
numberToNameComponent 1 = "one"
numberToNameComponent 2 = "two"
numberToNameComponent 3 = "three"
numberToNameComponent 4 = "four"
numberToNameComponent 5 = "five"
numberToNameComponent 6 = "six"
numberToNameComponent 7 = "seven"
numberToNameComponent 8 = "eight"
numberToNameComponent 9 = "nine"
numberToNameComponent 10 = "ten"
numberToNameComponent 11 = "eleven"
numberToNameComponent 12 = "twelve"
numberToNameComponent 13 = "thirteen"
numberToNameComponent 14 = "fourteen"
numberToNameComponent 15 = "fifteen"
numberToNameComponent 16 = "sixteen"
numberToNameComponent 17 = "seventeen"
numberToNameComponent 18 = "eighteen"
numberToNameComponent 19 = "nineteen"
numberToNameComponent 20 = "twenty"
numberToNameComponent 30 = "thirty"
numberToNameComponent 40 = "forty"
numberToNameComponent 50 = "fifty"
numberToNameComponent 60 = "sixty"
numberToNameComponent 70 = "seventy"
numberToNameComponent 80 = "eighty"
numberToNameComponent 90 = "ninety"
numberToNameComponent number = "COMPONENT ERROR " ++ (show number)