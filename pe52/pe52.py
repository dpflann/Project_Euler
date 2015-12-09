def is_permuted_multiple(n, limit=7):
  str_n = set(str(n))
  for i in range(2, limit):
    n_by_i = i * n
    if set(str(n_by_i)) != str_n:
      return False
  return True

def solve():
  i = 1
  while not is_permuted_multiple(i):
    i += 1
  # assumes it's possible to solve this... :)
  print("The smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x contains the same digits is %d" % i)

if __name__ == '__main__':
  solve()

