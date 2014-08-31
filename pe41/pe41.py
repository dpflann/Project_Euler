#!/usr/bin/python
# -*- coding: utf8 -*-
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

def primeGenerator():
  D = {}
  q = 2
  while True:
    if q not in D:
      yield q
      D[q * q] = [q]
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      del D[q]
    q = q + 1

def isPandigital(n, pandigitalTable):
  nStr = list(str(n))
  pDigits = set(map(str, pandigitalTable[len(nStr)]))
  nStr = set(nStr)
  if len(nStr) == len(pDigits):
    return (pDigits - nStr) == set([])
  else:
    return False

def findLargestPandigitalPrime(limit):
  primeGen = primeGenerator()
  prime = primeGen.next()
  pandigitalTable = { i: map(str,range(1, i + 1)) for i in range(1, 10) }
  largestPandigitalPrime = prime
  while prime <= limit:
    if isPandigital(prime, pandigitalTable) and prime > largestPandigitalPrime:
      largestPandigitalPrime = prime
    prime = primeGen.next()
  return largestPandigitalPrime

import math as m
def isPrime(n):
  for i in range(2, int(m.ceil(m.sqrt(n)))):
    if n % i == 0:
      return False
  return True

def fLpP(limit):
  largest = 0
  pandigitalTable = { i: map(str,range(1, i + 1)) for i in range(1, 10) }
  for n in range(limit, 0, -1):
    if n % 2 == 0:
      continue
    else:
      if isPrime(n) and isPandigital(n, pandigitalTable):
        if n >= largest:
          largest = n
        else:
          break
  return largest

def solve():
  limit = 987654321
  print "The largest n-digits pandigital prime is %d." % findLargestPandigitalPrime(limit)
