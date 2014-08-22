#!/usr/bin/python
# -*- coding: utf8 -*- 

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


import itertools as it

# http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
def partition(number):
  answer = set()
  answer.add((number, ))
  for x in range(1, number):
    for y in partition(number - x):
      answer.add((x, ) + y)
  return answer

def findPandigitalProducts():
  partitions = partition(9)
  partitions = [ p for p in partitions if len(p) == 3 ]
  partitions = [ p for p in partitions if p[2] >= 3 and p[2] <= 5 ]

  digits = "123456789"
  permutations = list(it.permutations(digits, 9))
  permutations = map(''.join, permutations)

  candidateProducts = set({})
  for p in permutations:
    for part in partitions:
      i_m1, i_m2, i_p = part
      m1, m2, product = digits = p[0:i_m1], p[i_m1:(i_m1 + i_m2)], p[(i_m1 + i_m2):]
      ints = map(int, [m1, m2, product])
      if ints[0] * ints[1] == ints[2]:
        candidateProducts.add(ints[2])
  sumOfProducts = sum(candidateProducts)
  return sumOfProducts

def solve():
  print "The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is %d." % findPandigitalProducts()

