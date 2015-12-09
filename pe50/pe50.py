def primes_sieve(limit):
  a = [True] * limit
  a[0] = a[1] = False
  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in range(i*i, limit, i):
        a[n] = False

def find_upper_limit(primes):
  i = 0
  while sum(primes[i:i+2]) < primes[-1]:
    i += 1
  return i

def find_prime_comprised_of_most_consecutive_primes(limit):
  prime = 0
  length = 0
  primes = list(primes_sieve(limit))
  cumulative_sums = [0] + [sum(primes[:i]) for i in range(1, len(primes) + 1) if sum(primes[:i]) < primes[-1]]
  _limit = primes[-1]
  primes = set(primes)
  i = 0
  while i < len(cumulative_sums):
    j = i - (length + 1)
    while j >= 0:
      diff = cumulative_sums[i] - cumulative_sums[j]
      dist = i - j
      if diff > _limit:
        break
      if diff in primes and dist > length:
        length = dist
        prime = cumulative_sums[i] - cumulative_sums[j]
      j -= 1
    i += 1
  return prime, length


def solve():
  prime, length = find_prime_comprised_of_most_consecutive_primes(1000000)
  print("The largest prime comprised of (%d) consecutive primes is : %d" % (length, prime))

if __name__ == "__main__":
  solve()
