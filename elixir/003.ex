# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

defmodule Euler do
  def primesUpTo(n) do
    [2,3,5,7,11]
  end

  def isPrime(n) do
    upper = :math.floor(:math.sqrt(n))
    if(n == 2 || n == 3) do
      true
    else
      false
    end
  end
end