#!/usr/bin/python
# -*- coding: utf8 -*-

# An irrational decimal fraction is created by concatenating the positive integers:
# 
#   0.123456789101112131415161718192021...
# 
#   It can be seen that the 12th digit of the fractional part is 1.
# 
#   If dn represents the nth digit of the fractional part, find the value of the following expression.
# 
#   d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def productOfDigits(indices):
  s = "_"
  i = 0
  highestIndex = max(indices)
  while len(s) <= highestIndex:
    s = s + ''.join(map(str, list(range(10**i, 10**(i + 1)))))
    i = i + 1
  total = reduce(lambda t, i: t * int(s[i]), indices, 1)
  return total

def solve():
  print "The value of d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000 is %d." % productOfDigits([1, 10, 100, 1000, 10000, 100000, 1000000])

if __name__ == '__main__':
  solve()
