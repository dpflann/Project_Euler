def find_max(limit=100):
    _max = 0
    for a in range(limit):
        for b in range(limit):
            num = a**b
            _sum = sum([int(i) for i in str(num)])
            if _sum > _max:
                _max = _sum
    return _max

def solve_2(limit=100):
    return max([(sum([int(i) for i in str(a**b)])) for a in range(limit) for b in range(limit)])

def solve():
  print("The greatest sum of digits from the result of a^b is: %d" % find_max())

if __name__ == '__main__':
  solve()
