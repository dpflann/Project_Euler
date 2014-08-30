#!/usr/bin/python
# -*- coding: utf8 -*-

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

def findFactorPairs(n):
  pairs = set({})
  if n % 2 == 0:
    n = n / 2
  for i in range(1, n):
    if n % i == 0:
      pairs.add(tuple(sorted( ( i, n / i ) )))
  return pairs

def findSideLengths(pairs, b):
  # b = 2mn
  # a = m**2 - n**2
  # c = m**2 + n**2
  sideTuples = []
  divisionFactor = 1
  if b % 2 == 1:
    divisionFactor = 2
  for p in pairs:
    n, m = p
    a = (m**2 - n**2) / divisionFactor
    c = (m**2 + n**2) / divisionFactor
    if a > 0 and c > 0:
      sideTuples.append((a, b, c))
  return sideTuples

def calculatePerimeter(sideTuple):
  return sum(sideTuple)

def findTriangles(limit):
  perimeterToTriangles = {}
  for b in range(1, limit):
    # find triangles
    pairs = findFactorPairs(b)
    lengths = findSideLengths(pairs, b)
    print "b: ", b, ", lengths: ", lengths
    perimeters = map(sum, lengths)
    print "perimeters: ", perimeters
    perimeters = filter(lambda p: p <= 1000, perimeters)
    print "perimeters: ", perimeters
    for p in perimeters:
      if p in perimeterToTriangles:
        perimeterToTriangles[p] += 1
      else:
        perimeterToTriangles[p] = 1
  maxGroupSize = 0
  mostPopularPerimeter = 0
  print perimeterToTriangles
  for k in perimeterToTriangles:
    if perimeterToTriangles[k] > maxGroupSize:
      maxGroupSize = perimeterToTriangles[k]
      mostPopularPerimeter = k
  return mostPopularPerimeter

def solve():
  print "The p <= 1000 for which the number of integral-side, right-angle triangles is maximized is %d." % findTriangles(120)
