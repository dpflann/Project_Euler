import math

def n_C_r(n=0, r=0):
  c_s = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
  return int(c_s)

def solve(n_limit=101, limit=1000000):
  return [n_C_r(n=i, r=r) > limit for i in range(1, n_limit) for r in range(1, i + 1)].count(True)

if __name__ == '__main__':
  print("The number of values of nCr greater than one-million when 1 <= n <= 100 is %d" % solve())
