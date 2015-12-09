def reverse_add(n):
    reverse_n = int(str(n)[::-1])
    return n + reverse_n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def solve(limit=10000):
    lychrel_numbers = set([])
    for n in range(1, limit + 1):
        i = 0
        _n = n
        while i < 50:
            r_n = reverse_add(n)
            if not is_palindrome(r_n):
                n = r_n
                i += 1
            else:
                break
        if i >= 50:
            lychrel_numbers.add(_n)
    print("The number of Lychrel numbers below %d is %d" % (limit, len(lychrel_numbers)))

if __name__ == '__main__':
  solve()
