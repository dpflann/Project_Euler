def find_distinct_prime_factors(n, primes):
  original = n
  prime_factors = set()
  for p in primes:
    while n % p == 0:
      prime_factors.add(p)
      n = n / p
    if n == 0:
      break
  return prime_factors

def find_consecutive_numbers_with_n_distinct_prime_factors(consecutive_numbers_required=4, distinct_prime_factors_required=4):
    primes = {2, 3, 5, 7}
    n = 10
    while True:
      if not any([n % p == 0 for p in primes]):
        primes.add(n)
      if len(find_distinct_prime_factors(n, primes)) == distinct_prime_factors_required:
        possible_consecutives = [n]
        n += 1
        while len(find_distinct_prime_factors(n, primes)) == distinct_prime_factors_required and len(possible_consecutives) < consecutive_numbers_required:
          possible_consecutives.append(n)
          n += 1
          if len(possible_consecutives) == distinct_prime_factors_required:
            return possible_consecutives 
      else:
          n += 1

def test_scenario():
  return find_consecutive_numbers_with_n_distinct_prime_factors(consecutive_numbers_required=3, distinct_prime_factors_required=3)

def solve():
  return find_consecutive_numbers_with_n_distinct_prime_factors(consecutive_numbers_required=4, distinct_prime_factors_required=4)[0]
