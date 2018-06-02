# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# for all integers [1..x], iteratively increasing x
# for list of [1..n] for n > 1, iteratively increasing n

def pandigital_concatination(x, n):
    return ''.join([str(x * a) for a in range(1,n+1)])

def is_pandigital(n):
    final = '123456789'
    output = ''.join(sorted(str(n)))
    return final == output

start_x = 1
end_x = 10000

start_n = 1
end_n = 7

numbers = [pandigital_concatination(a,b) for a in range(start_x,end_x) for b in range(start_n, end_n)]
other_numbers = sorted([int(x) for x in numbers if is_pandigital(x)])

value = other_numbers[-1]
print(value)
