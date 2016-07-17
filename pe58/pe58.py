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

#if __name__ == '__main__':
#  solve()

def is_composite(a,d,r,n):
  x = pow(a, d, n)
  if x == 1 or x == (n - 1):
    return False
  for i in range(r):
    if x == 1:
      return True
    if x == n - 1:
      return False
    x = pow(x, 2, n)

  return True

def miller_rabin(n):
  """
  When the number n to be tested is small, trying all a < 2(ln n)2 is not necessary, as much smaller sets of potential witnesses are known to suffice. For example, Pomerance, Selfridge and Wagstaff[8] and Jaeschke[9] have verified that

  if n < 2,047, it is enough to test a = 2;
  if n < 1,373,653, it is enough to test a = 2 and 3;
  if n < 9,080,191, it is enough to test a = 31 and 73;
  if n < 25,326,001, it is enough to test a = 2, 3, and 5;
  if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
  if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
  if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
  if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
  if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.
  """
  small_witnesses = [2, 3, 5, 7, 11]
  d = n - 1
  r = 0
  while d % 2==0:
    d /= 2
    r += 1

  for a in small_witnesses:
    if is_composite(a, d, r, n):
      return False

  return True

primes_on_diagonal = 3
numbers_on_diagonal = 5

ratio = primes_on_diagonal/float(numbers_on_diagonal)

i = 5
while ratio >= 0.1:
  inc = i-1
  numbers_on_diagonal +=4
  for j in range(1,4):
    if miller_rabin(i**2-inc*j):
      primes_on_diagonal+=1
  ratio = primes_on_diagonal/float(numbers_on_diagonal)
  i += 2

#checks ratio at the beginning of the loop, so we went 2 too far
print(i-2)
