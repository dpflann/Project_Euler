
# try a a b
# n**2 + a*b + b
# (-1000, 1000)
from itertools import product

def primes_sieve(limit):
  a = [True] * limit                          # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False

primes = list(primes_sieve(1000000))

limit_on_b = [p for p in primes if p < 1000]
pairs = product(range(-999, 1000), limit_on_b)

def find_consecutive_primes(a, b):
  consecutive_primes = []
  # n = 0 --> 0**2 + a*0 + b = b
  prime = b
  n = 1
  while prime in primes:
    consecutive_primes.append(prime)
    prime = n**2 + a*n + b
    n += 1
  #print("n = %d for %d and %d" % (n, a, b))
  return n - 1, consecutive_primes

def try_pairs(pairs):
  results = []
  for a, b in pairs:
    n_limit, consecutive_primes = find_consecutive_primes(a, b)
    results.append(((a, b), len(consecutive_primes)))
  return results

def find_max_pair_product(pairs):
  a, b = max(try_pairs(pairs), key=lambda t: t[1])[0]
  return a * b

if __name__ == '__main__':
  print "The product of a, b is: %d" % find_max_pair_product(pairs)
