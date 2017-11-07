# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
# 
#   It can be verified that the sum of the numbers on the diagonals is 101.
# 
#   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def sumOfDiagonals(sideLength):
  sumOfDiagonals = 1
  if sideLength == 1:
    return sumOfDiagonals
  if sideLength < 1:
    return -1
  squareSeeds = range(3, sideLength + 1, 2)
  for seed in squareSeeds:
    previousSeed = seed - 2
    wallOfNumbers = range(previousSeed ** 2 + 1, seed ** 2 + 1)
    for i in range(previousSeed, len(wallOfNumbers), previousSeed + 1):
      sumOfDiagonals = sumOfDiagonals + wallOfNumbers[i]
  return sumOfDiagonals

def solve():
  print "The sum of the numbers on the diagonals in a 1001x1001 spiral is %d." % sumOfDiagonals(1001)

def test():
  assert(sumOfDiagonals(1) == 1)
  assert(sumOfDiagonals(3) == 25)
  assert(sumOfDiagonals(5) == 101)
  print "Tests pass"

if __name__ == '__main__':
  solve()
