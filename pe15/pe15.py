# Moving only left and right, how many paths exist from the top-left corner to the bottom-right corner in a 20x20 grid?

import math

def paths(r=20, c=20):
  f = math.factorial
  return f((r) + (c)) / (f(r) * f(c))

def test():
  assert(paths(2, 2) == 6)
  assert(paths(1,1) == 2)


test()

def solve():
  print("Number of paths in 20x20 grid = %d" % paths())

solve()


