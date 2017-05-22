# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindromicNumber(n)
  n == n.to_s.reverse.to_i
end

threeDigitNumbers = (100..999).to_a

largestPalindrome = 0

threeDigitNumbers.each do |firstNum| 
  threeDigitNumbers.each do |secondNum| 
    num = firstNum * secondNum
    if isPalindromicNumber(num) && num > largestPalindrome
      largestPalindrome = num
    end
  end
end
puts largestPalindrome
