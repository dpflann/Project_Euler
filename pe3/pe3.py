#!/usr/bin/python3 

import math

LIMIT = 600851475143

def primes_sieve(limit):
  a = [True] * limit                          # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False

primes = list(primes_sieve(int(math.ceil(math.sqrt(LIMIT)))))
factors = [p for p in primes if LIMIT % p == 0]

print('The largest prime factor of %d is %d.' % (LIMIT, max(factors)))
