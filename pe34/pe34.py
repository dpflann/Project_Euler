#!/usr/bin/python
# -*- coding: utf8 -*-

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math as m
from matplotlib import pyplot
from numpy import arange
def scatterplot(x,y):
  pyplot.plot(x,y,'b.')
  pyplot.xlim(min(x)-1,max(x)+1)
  pyplot.ylim(min(y)-1,max(y)+1)
  pyplot.show()


factorialTable = { i: m.factorial(i) for i in range(0, 10) }
def sumFactorialOfDigits(n, factorialTable):
  Sum = 0
  while n > 0:
    digit = n % 10
    Sum = Sum + factorialTable[digit]
    n = n / 10
  return Sum

def explore(limit, lower=10):
  xs = []
  ys = []
  for i in range(lower, limit):
    sFoD = sumFactorialOfDigits(i, factorialTable)
    xs.append(i)
    ys.append(sFoD)
  scatterplot(xs, ys)
  return xs, ys

def sumOfFactorialOfDigits(n):
  factorialTable = { i: m.factorial(i) for i in range(0, 10) }
  numbers = []
  for i in range(10, n):
    sFoD = sumFactorialOfDigits(i, factorialTable)
    if sFoD == i:
      numbers.append(i)
  return sum(numbers)

# intuitively limit seems to be 9! so use it as upper bound
# TODO: explore this idea more mathematically
def solve():
  print "The sum of all numbers which are equal to the sum of the factorial of their digits is %d." % sumOfFactorialOfDigits(m.factorial(9))

if __name__ == '__main__':
  solve()
