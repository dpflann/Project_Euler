# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a not equal b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math as m

def sumDivisors(n):
  sumOfDivisors = 0
  i = 1
  while i < n:
    if n % i == 0:
      sumOfDivisors = sumOfDivisors + i
    i = i + 1
  return sumOfDivisors

def findAmicablePairs(sumTable):
  amicablePairs = []
  for n in sumTable:
    a = n
    aSum = sumTable[a]
    if aSum in sumTable:
      b = aSum
      bSum = sumTable[b]
      if bSum == a:
        if a not in amicablePairs and b not in amicablePairs and a != b:
          amicablePairs = amicablePairs + [ a, b ]
  return amicablePairs

def sumAmicablePairs(n):
  sumTable = {}
  for i in range(1, n + 1):
    sumTable[i] = sumDivisors(i)
  amicablePairs = findAmicablePairs(sumTable)
  sumOfPairs = sum(amicablePairs)
  return sumOfPairs

def solve():
  print "The sum of all the amicable numbers under 1000 is %d." % sumAmicablePairs(10000)

def test():
  assert(sumDivisors(16) == 15)
  assert(sumDivisors(853) == 1)
  pairs1 = findAmicablePairs( { 220 : 284, 284 : 220 } )
  pairs1.sort()
  assert(pairs1 == [ 220, 284 ])
  assert(sumAmicablePairs(10) == 0)
  assert(sumAmicablePairs(300) == ( 220 + 284 ))
  print "Tests Pass"

if __name__ == '__main__':
  solve()
