from math import sqrt

def is_hexagonal(N):
  # 2n^2 - n - N = 0
  n = (1 + sqrt(1 + 4*2*N)) / 4
  return n == int(n)

def is_pentagonal(N):
  # 3n^2 - n - 2N = 0
  n = (1 + sqrt(1 + 4*3*2*N)) / 6
  return n == int(n)

def triangular_number(n):
  return int((n * (n + 1)) / 2)

def find_next_triangular_number(n):
  found_next = False
  while True:
    T_n = triangular_number(n)
    if is_hexagonal(T_n) and is_pentagonal(T_n):
      return T_n
    n += 1

def solve(lower_bound=286):
  print("The next triangular number that is pentagonal and hexagonal is: %d" % find_next_triangular_number(lower_bound))

if "__main__" == __name__:
  solve()
