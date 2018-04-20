# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def is_prime(n):
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    limit = int(n ** (.5)) + 1
    for i in range(3,limit,2):
        if n % i == 0:
            return False
    return True

n = 3
count = 2
limit = 10001
while count < limit:
    n += 2
    if is_prime(n):
        count += 1

value = n
print(value)
print(value == 104743)
