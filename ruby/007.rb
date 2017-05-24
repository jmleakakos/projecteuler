# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

require 'prime'

PRIME_COUNT_SEARCH = 10001

puts "THIS IS A DIRTY CHEAT: " + Prime.first(PRIME_COUNT_SEARCH).last.to_s

def isPrime(n)
  if n == 2
    return true
  end
  if n % 2 == 0
    return false
  end
  upperBound = Math.sqrt(n).floor
  (2..upperBound).none? { |i| n % i == 0 }
end

def primesUpToCount(n)
  primeCount = 1
  currentPrime = 2
  nextPrimeCandidate = 3
  while primeCount < n
    if isPrime(nextPrimeCandidate)
      currentPrime = nextPrimeCandidate
      primeCount += 1
    end
    # loop through all odd numbers for now
    # implement some kind of seive if this isn't fast enough
    nextPrimeCandidate += 2
  end
  currentPrime
end

puts "THIS IS REAL: " + primesUpToCount(PRIME_COUNT_SEARCH).to_s
