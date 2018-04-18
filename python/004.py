# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return n == int(str(n)[::-1])

numbers = range(100,1000)
products = [x*y for x in numbers for y in numbers if is_palindrome(x*y)] 
largest = 0

for n in products:
    if n > largest:
        largest = n

value = largest
print(value)
print(value == 906609)
