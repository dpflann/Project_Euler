#The following iterative sequence is defined for the set of positive integers:
#
#  n -> n/2 (n is even)
#  n -> 3n + 1 (n is odd)
#
#  Using the rule above and starting with 13, we generate the following sequence:
#
#    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#    Which starting number, under one million, produces the longest chain?
#
#    NOTE: Once the chain starts the terms are allowed to go above one million.

import sys

collatz_lengths = { 0:0, 1:1 }
def collatz(n):
  if (n % 2 == 0):
    if n in collatz_lengths:
      return collatz_lengths[n]
    else:
      collatz_lengths[n] = 1 + collatz(n / 2)
      return collatz_lengths[n]
  else:
    if n in collatz_lengths:
      return collatz_lengths[n]
    else:
      collatz_lengths[n] = 1 + collatz(3*n + 1)
      return collatz_lengths[n]


def longest_collatz(n):
  print("Finding the number less than or equal to {0} with the longest collatz sequence.".format(n))
  _max = (-1, -1)
  for i in range(0, n):
    c = collatz(i)
    if c > _max[1]:
      _max = (i, c)

  return _max

if (len(sys.argv) > 1):
  print(longest_collatz(int(sys.argv[1])))
else:
  print(longest_collatz(1000000))

