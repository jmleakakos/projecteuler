# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def decimal_to_binary(n):
    d,m = divmod(n,2)
    if d == 0:
        return str(m)
    else:
        return(decimal_to_binary(d) + str(m))

start = 1
end = 1000000

ns = [n for n in range(start,end) if is_palindrome(n) and is_palindrome(decimal_to_binary(n))]


value = sum(ns)
print(value)
