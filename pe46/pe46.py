def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-primes_sieve
                a[n] = False
 
def find_smallest_non_goldbach(limit=1000):
    primes = list(primes_sieve(limit))
    square_tables = set([2*n**2 for n in range(1, limit)])
    N = 9
    while True:
        if N not in primes and not any([N - p in square_tables for p in primes]):
            return N
        N += 2

def find_smallest_non_goldbach_2():
    primes = {2, 3, 5, 7}
    n = 9
    while True:
        if not any([n % p == 0 for p in primes]):
            primes.add(n)
        elif not any([n - (2 * i**2) in primes for i in range(1, n)]):
            return n
        n += 2

