# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def digits(n):
    return [int(x) for x in str(n)]

first_set = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def write_out(n):
    ds = digits(n)
    if n == 0:
        return 'zero'
    if n <= 20:
        return first_set[n]
    if n < 100:
        return first_set[ds[0] * 10] + first_set[ds[1]]
    if n < 1000:
        hundreds_digit = ds[0]
        tens_digit = ds[1]
        ones_digit = ds[2]
        hundreds = first_set[hundreds_digit] + 'hundred' 
        if tens_digit == 0 and ones_digit == 0:
            return hundreds
        if (tens_digit == 0 or tens_digit == 1):
            return hundreds + 'and' + first_set[int(str(tens_digit) + str(ones_digit))]
        if (tens_digit > 1):
            return hundreds + 'and' + first_set[tens_digit * 10] + first_set[ones_digit]
        return hundreds 
    return 'onethousand'

start = 1
end = 5
end = 1000



numbers = range(start, end+1)
written_out = [write_out(x) for x in numbers]
total = sum([len(x) for x in written_out])


value = total
print(value)
print(value == 21124)

