-- Smallest multiple
-- Problem 5 
-- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
-- 
-- What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
--
-- LCM of [1..20]

import qualified Data.Map.Strict as Map
import Data.Numbers.Primes
import Data.List

baseMap :: Map.Map Int Int
baseMap = Map.empty

numbers = [2..20]

main = do
  let primeFactorLists = map primeFactors numbers
  let primeFactorMaps = map generatePrimeFactorMap primeFactorLists
  let lcmMap = Map.unionsWith greater primeFactorMaps
  print $ Map.foldrWithKey (\k val acc -> acc * (k ^ val)) 1 lcmMap

checkMapAndReturnFinalValue :: Map.Map Int Int -> Int -> Int -> Map.Map Int Int
checkMapAndReturnFinalValue primePowerMap prime power = Map.insert prime finalValue primePowerMap
  where maybePower = Map.lookup prime primePowerMap
        finalValue = check maybePower power
        check (Just a) b = if a > b then a else b
        check Nothing b = b

generatePrimeFactorMap primeFactorsList = primeFactorMap
  where grouped = group primeFactorsList
        primeFactorMap = foldr (\val acc -> Map.insert (head val) (length val) acc) Map.empty grouped

greater = (\a b -> if a > b then a else b)
