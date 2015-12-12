def find_passcode():
  with open('p079_keylog.txt', 'r') as f:
    partial_passcodes = f.read().split('\n')
  # For digit, I want to consider how many times it occurs before other digits
  used_digits = set(''.join(partial_passcodes))
  digits = {d:{_d:0 for _d in used_digits if _d != d} for d in used_digits}
  for p in partial_passcodes:
    for i in range(len(p)):
      current = p[i]
      preceding = p[:i]
      for _p in preceding:
        digits[current][_p] += 1
  precedents_ranking = {}
  for d, v in digits.items():
    non_zeros = [_v for _v in v.values() if _v > 0]
    precedents_ranking[d] = non_zeros
  precedents_ranking = sorted(precedents_ranking.items(), key=lambda t: len(t[1]))
  return ''.join([t for t, r in precedents_ranking])

def solve():
  print("The shortest possible secret passcode is %s" % find_passcode())

if __name__ == '__main__':
  solve()
