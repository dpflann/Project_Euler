# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 
#   012   021   102   120   201   210
# 
#   What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math as m

def findIthPermutation(ith, numbers=range(0,10) ):
  s = [ ]
  start = max(numbers)
  for pos in range(start, 0, -1):
    permutationsAtPosition = m.factorial(pos)
    n = 0
    while ith > 0:
      ith = ith - permutationsAtPosition
      n = n + 1
    if ith < 0:
      ith = ith + permutationsAtPosition
    numberForCurrentPosition = numbers[n - 1]
    s.append(numberForCurrentPosition)
    numbers.remove(numberForCurrentPosition)
  s.append(numbers[0])
  return ''.join(map(str, s))

def test():
  assert(findIthPermutation(1, range(0, 3)) == "012")
  assert(findIthPermutation(2, range(0, 3)) == "021")
  assert(findIthPermutation(3, range(0, 3)) == "102")
  assert(findIthPermutation(4, range(0, 3)) == "120")
  assert(findIthPermutation(5, range(0, 3)) == "201")
  assert(findIthPermutation(6, range(0, 3)) == "210")
  print "Tests Pass!"

def solve():
  print "The millionth lexicographic permutation of the digiits 0, 1, 2, 4, 5, 6, 7, 8, 9 is %s." % findIthPermutation(1000000)

if __name__ == '__main__':
  solve()
