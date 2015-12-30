import math

def find_layer_with_ratio(PRIME_RATIO=.10):
  """
  The ratio of primes to diagonals does stabalize to a monotonically decreasing ratio
  until after adding a layer with side length of 9.
  n = 1 -->  (0 / 1) = 0
  n = 3 -->  (3 / 5) = .600000
  n = 5 -->  (5 / 9) = .55555
  n = 7 -->  (8 / 13) = .61538
  n = 9 -->  (9 / 17) = .52941
  n = 11 --> (10 / 21) = .47619
  """
  p = 8.0
  d = 13.0
  n = 7
  last_corner = 49
  while (p / d) > PRIME_RATIO:
    n += 2
    layer = range(last_corner + 1, n**2 + 1)
    corners = layer[-1::(1 - n)]
    p_s = [c for c in corners if is_prime(c)]
    p += len(p_s)
    d += 4
    last_corner = n**2
  return n

def is_prime(p):
  for i in range(2, int(math.ceil(math.sqrt(p))) + 1):
    if p % i == 0:
      return False
  return True

def test():
  assert(find_layer_with_ratio(PRIME_RATIO=(8.0 / 13.0)) == 7)
  assert(find_layer_with_ratio(PRIME_RATIO=(9.0 / 17.0)) == 9)
  assert(find_layer_with_ratio(PRIME_RATIO=(10.0 / 21.0)) == 11)
  assert(find_layer_with_ratio(PRIME_RATIO=.5) == 11)

def solve():
  print("The side-length of the layer where the ratio of primes to composites in occurring in the diagonals is less than .10 is %d" % find_layer_with_ratio())

if __name__ == '__main__':
  solve()
