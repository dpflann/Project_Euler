import sys

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

def find_top_heavy_expansions_count(number_of_expansions=1000):
  count = 0
  previous_numerator = 3
  previous_denominator = 2
  for _ in range(number_of_expansions - 1):  # account for seeding with first expansion
    next_numerator = previous_numerator + 2 * previous_denominator
    next_denominator = previous_numerator + previous_denominator
    if len(str(next_numerator)) > len(str(next_denominator)):
      count += 1
    previous_numerator, previous_denominator = next_numerator, next_denominator
  return count

def solve():
  count = 0
  if len(sys.argv) == 2:
    if sys.argv[1] == '1':
      expansions, count = find_top_heavy_expansions()
    elif sys.argv[1] == '2':
      count = find_top_heavy_expansions_count()
  else:
    count = find_top_heavy_expansions_count()
  print('In the first 1000 expansions of 2^(1/2) as a continued fraction, the number of fractions with a numerator longer than the denominator is %d' % count)

if __name__ == '__main__':
  solve()

