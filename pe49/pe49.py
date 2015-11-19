import itertools
from collections import defaultdict

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-primes_sieve
                a[n] = False

def prime_permutations():
  primes = primes_sieve(10000)
  primes = {p for p in primes if p > 1000}
  solutions = set() 
  for p in primes:
    permutations = set(map(lambda s: int(''.join(s)), itertools.permutations(str(p), 4)))
    possible_permutations = permutations & primes
    possible_permutations = sorted(list(possible_permutations))
    if len(possible_permutations) >= 3:
      diffs = defaultdict(set)
      for (i, perm_1) in enumerate(possible_permutations, start=1):
        for perm_2 in possible_permutations[i:]:
          diffs[perm_2 - perm_1].add(perm_1)
          diffs[perm_2 - perm_1].add(perm_2)
      for d, s in diffs.items():
        if len(s) == 3:
          solutions.add(tuple(sorted(tuple(s))))
  return solutions - set([(1487, 4817, 8147)])

def concatenated_prime_permutations():
  return ''.join(sorted(map(str, prime_permutations().pop())))

def solve():
  print("The 12-digit number from the concatenated 3 terms in sequence is: %s" % concatenated_prime_permutations())

if __name__ == "__main__":
  solve()
