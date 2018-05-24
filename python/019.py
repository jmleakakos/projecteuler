# You are given the following information, but you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date, timedelta


current_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)
counter = 0

day_increment = timedelta(days=1)

while current_date < end_date:
    if current_date.weekday() == 6 and current_date.day == 1:
        counter += 1
    current_date += day_increment
    

number_of_sundays = counter 
value = number_of_sundays
print(value)
