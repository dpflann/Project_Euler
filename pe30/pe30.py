#!/usr/bin/python

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#   1634 = 14 + 64 + 34 + 44
#   8208 = 84 + 24 + 04 + 84
#   9474 = 94 + 44 + 74 + 44
#   As 1 = 14 is not a sum it is not included.
#
#   The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#   Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def addToSet(aSet):
  def _add(i):
      aSet.add(i)
  return _add

def isSumOfPowerOfDigits(n, power):
  digits = list(str(n))
  sumOfDigits = reduce(lambda theSum, digit: theSum + ( int(digit) )**power, digits, 0)
  return sumOfDigits == n

def findDigitPowers(power):
  numbers = set({})
  maxNumber = 10
  length = 3 # start with 3 digits numbers
  foundLimit = False
  while not foundLimit:
    # print "length, maxNumber, numbers: ", length, maxNumber, numbers
    currentNumbers = [ i for i in range(maxNumber, length * (9**power)) if isSumOfPowerOfDigits(i, power) ]
    if len(currentNumbers) > 0:
      currentMax = max(currentNumbers)
      # print "currentNumbers, currentMax: ", currentNumbers, currentMax
      map(addToSet(numbers), currentNumbers)
      if currentMax > maxNumber:
        maxNumber = currentMax
      elif currentMax == maxNumber: # found the limit?
        foundLimit = True
    length = length + 1
  return sum(numbers)

def fDp(power):
  return sum({ i for i in range(10, 9**(power + 1)) if reduce(lambda theSum, digit: theSum + ( int(digit) )**(power), list(str(i)), 0) == i })

def solve():
  print "The sum of all the numbers that can be written as the sum of the fifth powers of their digits is %d." % findDigitPowers(5)
  print "The sum of all the numbers that can be written as the sum of the fifth powers of their digits is %d." % fDp(5)

if __name__ == '__main__':
  solve()
