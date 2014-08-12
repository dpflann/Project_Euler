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

def firstMondays():
    firstsOnMondays = 0
    startDay = 1
    for year in range(1901, 2001):
        for month in range(1, 13):
            if startDay == 1:
                firstsOnMondays = firstsOnMondays + 1
            d = getDaysInMonth(month, year)
            offset = d % 7
            startDay = (startDay + offset) % 7
    return firstsOnMondays 

def getDaysInMonth(month, year):
    monthsMap = { 1 : 31,
                  3 : 31,
                  4 : 30,
                  5 : 31,
                  6 : 30,
                  7 : 31,
                  8 : 31,
                  9 : 30,
                  10 : 31,
                  11 : 30,
                  12 : 31 }
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                    return 29
            else:
                return 29
        else:
            return 28
    return monthsMap[month]


def solve():
    print("The total number of months that began on Mondays between 1/1/1901 and 12/31/2000 is %d." % firstMondays())

solve()
