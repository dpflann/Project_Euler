def find_top_heavy_expansions(number_of_expansions=1000):
  count = 0
  expansions = [(3,2)]
  for _ in range(number_of_expansions - 1):  # account for seeding with first expansion
    previous_numerator, previous_denominator = expansions[-1]
    next_numerator = previous_numerator + 2*previous_denominator
    next_denominator = previous_numerator + previous_denominator
    expansions.append((next_numerator, next_denominator))
    if len(str(next_numerator)) > len(str(next_denominator)):
      count += 1
  return expansions, count

def solve():
  expansions, count = find_top_heavy_expansions()
  print('In the first 1000 expansions of 2^(1/2) as a continued fraction, the number of fractions with a numerator longer than the denominator is %d' % count)


if __name__ == '__main__':
  solve()

