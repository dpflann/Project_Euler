#!/usr/bin/python
# -*- coding: utf8 -*-

#### Circular Primes ####
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import math as m

def sieve(n):
  limit = m.sqrt(n)
  primeTable = { num: True for num in range(2, n + 1) }
  for i in range(2, int(m.floor(limit) + 1)):
    if primeTable[i] == True:
      iSquared = i**2
      for j in range(iSquared, n + 1, i):
        primeTable[j] = False
  return [ k for k in primeTable.keys() if primeTable[k] == True ]

import itertools as it
def rotations(n):
  digits = list((str(n)))
  rotations = []
  previousRotation = digits
  for i in range(0, len(digits)):
    rotation = [previousRotation[-1]] + previousRotation[0:-1]
    rotations.append(rotation)
    previousRotation = rotation
  rotations = map(lambda r: int(''.join(r)), rotations)
  return rotations

def isPrime(n):
  for i in range(2, int(m.ceil(m.sqrt(n)))):
    if n % i == 0:
      return False
  return True

def isPrimeCircular(p):
  primeRotations = rotations(p)
  return len(filter(lambda p: isPrime(p), primeRotations)) == len(primeRotations)

def findCircularPrimesLessThan(n):
  primes = sieve(n)
 # print "Primes: ", primes
  circularPrimes = filter(isPrimeCircular, primes)
 # print "Circular Primes: ", circularPrimes
  return len(circularPrimes)

def solve():
  oneMillion = 1000000
  print "The number of circular primes below one million is %d." % findCircularPrimesLessThan(oneMillion)

if __name__ == '__main__':
  solve()
