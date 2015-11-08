# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def find_concatenated_pandigital(LIMIT=10000):
  _max = 0
  for i in range(1, LIMIT):
    n = 2
    _p = 0
    while len(str(_p)) < 10:
      _p = int(''.join([str(i * j) for j in range(1, n + 1)]))
      if is_pandigital(_p) and _p > _max:
        _max = _p
      n += 1
  return _max

def is_pandigital(p):
  p_str = str(p)
  return len(p_str) == 9 and all([p_str.count(i) == 1 for i in '123456789'])

LIMIT=100000

def solve():
  print("The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,3,..,n) where n > 1 is: %d" % find_concatenated_pandigital(LIMIT=LIMIT))
