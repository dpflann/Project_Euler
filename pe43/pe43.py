# Sub-string divisibility

import itertools

def has_substring_divisibility(n):
  """Input is a string."""

  substring_divisors = {
      (2, 4): 2,
      (3, 5): 3,
      (4, 6): 5,
      (5, 7): 7,
      (6, 8): 11,
      (7, 9): 13,
      (8, 10): 17
  }
  #n_str = str(n)
  #return all([int(n_str[t[0] - 1:t[1]]) % d == 0 for t, d in substring_divisors.items()])
  return all([int(n[t[0] - 1:t[1]]) % d == 0 for t, d in substring_divisors.items()])

def find_substring_divisible_pandigitals():
  pandigital_numbers = [''.join(p) for p in list(itertools.permutations('0123456789')) if p[0] != '0']
  pandigital_numbers_with_substring_divisibility = [p for p in pandigital_numbers if has_substring_divisibility(p)]
  return pandigital_numbers_with_substring_divisibility

def solve():
  print("The sum of pandigital numbers with substring divisibility is: %d" % sum(map(int, find_substring_divisible_pandigitals())))

def test():
  assert(has_substring_divisibility(1406357289) == True)

if __name__ == '__main__':
  solve()

