-- Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
-- 
-- For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
-- 
-- What is the total of all the name scores in the file?

import Data.Maybe (fromJust)
import Data.List (elemIndex, sort)
import Data.List.Split (wordsBy)

charValue c = (fromJust $ elemIndex c ['A'..'Z']) + 1

alphabeticalValue = sum . map charValue

main = do
  namesText <- readFile "022-names.txt"
  let names = sort $ wordsBy (\c -> c == ',') $ filter (/='"') namesText
  let namesValues = map alphabeticalValue names
  let namesValuesWithIndex = map (\(i, v) -> i*v) $ zip [1..] namesValues
  print $ sum namesValuesWithIndex
