# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def sumDivisors(n):
  sumOfDivisors = 0
  i = 1
  while i < n:
    if n % i == 0:
      sumOfDivisors = sumOfDivisors + i
    i = i + 1
  return sumOfDivisors

def isAbundant(n):
  return sumDivisors(n) > n

def sumOfNonAbundantSumNumbers():
  upperLimit = 28123
  # find all the abundant numbers in this range
  abundantNumbers = [ n for n in range(1, upperLimit + 1) if isAbundant(n) ]

  import itertools as it
  totalSumUpToLimit = (upperLimit * (upperLimit + 1)) / 2
  # find all numbers up to 28123 that are sums of abundant numbers
  pairs = list(it.product(abundantNumbers, abundantNumbers))
  dualAbundantNumbersLessThanUpperLimit = { n for n in set(map(lambda n: n[0] + n[1], pairs)) if n < upperLimit + 1 }
  result = totalSumUpToLimit - sum(dualAbundantNumbersLessThanUpperLimit)
  return result

def solve():
  print "The sum of all the positive integers which cannot be written as the sum of two abundant numbers is %d." % sumOfNonAbundantSumNumbers()

if __name__ == '__main__':
  solve()
