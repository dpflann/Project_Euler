def convergent(terms):
  if len(terms) == 1:
    return terms[0]
  base = terms[0]
  numerator = 1
  denominator = terms[-1]
  for n in terms[-2:0:-1]:
    expanded_numerator = n * denominator + numerator
    numerator = denominator
    denominator = expanded_numerator

  return (2 * denominator + numerator, denominator)

def expand_e_to_nth_convergent(n):
  base_exp = []
  l = 1
  i = 1
  while l < n:
    base_exp.extend([1, 2*i, 1])
    i += 1
    l += 3
  return [2] + base_exp[:n]

def sum_of_numerator_digits_in_expansion(n):
  numerator, denominator = convergent(expand_e_to_nth_convergent(n))
  return sum(map(int, str(numerator)))

def solve():
  print('The sum of the digits in the numerator of the 100th convergent of e is: %d' % sum_of_numerator_digits_in_expansion(100))


if __name__ == '__main__':
  solve()
