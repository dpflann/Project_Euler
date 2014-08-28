#!/usr/bin/python
# -*- coding: utf8 -*-

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#   It is possible to make £2 in the following way:
#
#   1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#   How many different ways can £2 be made using any number of coins?

class Memoize:
  def __init__(self, f):
    self.f = f
    self.memo = {}
  def __call__(self, *args):
    if not args in self.memo:
      self.memo[args] = self.f(*args)
    return self.memo[args]


def findWaysForSum(coins, targetSum):
  if targetSum == 0:
    return 1
  if len(coins) == 0 or targetSum < 0:
    return 0
  else:
    currentMax = max(coins)
    return findWaysForSum(coins, targetSum - currentMax) + findWaysForSum(coins - frozenset({ currentMax }), targetSum)

def findDifferentWaysToSum(n):
  coins = frozenset({ 1, 2, 5, 10, 20, 50, 100, 200 })
  return Memoize(findWaysForSum)(coins, n)
