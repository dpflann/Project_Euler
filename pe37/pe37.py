# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# 
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import math

def primes_sieve(limit):
  a = [True] * limit                          # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False

primes = list(primes_sieve(1000000))

def truncate_left(n, acceptable):
  power = int(math.log10(n))
  while power >= 0:
    if n not in acceptable:
      return False
    n = n % (10**power)
    power -= 1
  return True

def truncate_right(n, acceptable):
  while n > 0:
    if n not in acceptable:
      return False
    n = n / 10
  return True

def is_both_truncatable(n, acceptable):
  if n not in [2, 3, 5, 7]:
    is_right = truncate_right(n, acceptable)
    if is_right:
     return truncate_left(n, acceptable)
  else:
    return False

def find_truncatable(primes):
  eligible_primes = [p for p in primes if is_both_truncatable(p, primes)]
  return eligible_primes

def test():
  n = 3797
  acceptable = [3797, 797, 379, 97, 37, 7, 3]
  assert(True == truncate_left(n, acceptable))
  assert(True == truncate_right(n, acceptable))
  assert(True == is_both_truncatable(n, acceptable))

def solve():
  eligible_primes = find_truncatable(primes)
  if len(eligible_primes) == 11:
    print("The sum of the 11 primes that are both left and right truncatable is: %d" % sum(eligible_primes))
  else:
    print("Not enough primes", eligible_primes)

if __name__ == '__main__':
  solve()
