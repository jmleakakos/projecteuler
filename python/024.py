# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
# 012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


from itertools import permutations


def digits_to_number(digits):
    reversed_digits = reversed(digits)
    output = 0
    for i,v in enumerate(reversed_digits):
        output += v * 10 ** i
    return output
    
digits = range(0,3)
digits = range(0,10)

ps = permutations(digits)
output = [digits_to_number(p) for p in ps]
output.sort()


value = output[999999]
print(value)
print(value == 2783915460)
