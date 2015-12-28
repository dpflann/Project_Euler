"""
The length of a base raised to n is equal to:
  math.ceil(math.log(x**n, 10))
We must consider when:
  length of x**n = n
What are the bounds?
  math.ceil(math.log(x**n, 10)) = n
  =>
  n * math.log(x, 10) + 1 >= n, therefore x <= 10**((n - 1) / n)
  
  and

  n * math.log(x, 10) < n, therefore x < 10

  The bounds then are:
  10**((n - 1) / n) <= x < 10

  We are dealing with integers, x = 9 is the true max.
  And math.ceil(10**((n - 1) / n)) is the true minimum.

  This relation means:
  For a given power n, the possible bases such that x**n are the integers in the range:
  [math.ceil(10**((n - 1) / n)), 9], the count: 9 - min + 1
"""

import sys
import math

def find_powerful_numbers_brute():
  """
  1**1 is the beginning. Then 2, 9 are conidered. 9**21 is the last 9**n s.t. len(str(9**n)) = n
  """
  return len([1] + [i**n for i in range(2, 10) for n in range(1, 22) if len(str(i**n)) == n])

def find_powerful_numbers_informed():
  n = 1
  count = 0
  while min_base(n) <= 9:
    count += 9 - min_base(n) + 1  # count the integers between 9 (max) and min_x
    n += 1
  return int(count)

def min_base(n):
  n_fl = float(n)
  return math.ceil(10.0**((n_fl - 1) / n_fl))

def solve():
  solution = None
  if sys.argv[1] == '1':
    solution = find_powerful_numbers_brute()
  elif sys.argv[1] == '2':
    solution = find_powerful_numbers_informed()
  else:
    solution = find_powerful_numbers_informed()
  print("The number of n-digit positive integers that are also n-th powers is: %d" % solution)

if __name__ == '__main__':
  solve()
