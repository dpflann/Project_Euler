# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#
# Fully Reptend Primes:
#   1. http://mathworld.wolfram.com/FullReptendPrime.html
#   2. http://oeis.org/A001913

def findLongestCycle(n):
  longestCycle = -1
  denominator = -1
  for d in range(n, 1, -1):
    remainders = {}
    if d % 2 != 0:
      dividend = 1
      decimalPosition = 0
      while dividend not in remainders:
        remainders[dividend] = decimalPosition
        dividend = 10 * (dividend % d)
        decimalPosition = decimalPosition + 1
      decimalPosition = decimalPosition - 1
      if decimalPosition == d - 1:
        if decimalPosition > longestCycle:
          longestCycle = decimalPosition
          denominator = d
        else:
          break
  return denominator, longestCycle

def test():
  assert(findLongestCycle(7) == (7, 6))
  assert(findLongestCycle(63) == (61, 60))
  assert(findLongestCycle(100) == (97, 96))
  print "Tests Pass"

def solve():
  d, length = findLongestCycle(1000)
  print "The value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part is %d with length %d." % (d, length)

if __name__ == '__main__':
  solve()
