from math import sqrt
def is_pentagonal(N):
    # P_n = n(3n-1)/2 => (3/2)n^2 - (1/2)n - N = 0 = 3n^2 - n - 2N = 0
    # n = (1 + math.sqrt(1 + 4*3*2N)) / 2(3)
    value = (1 + sqrt(1 + 4*3*2*N)) / 6
    return value == int(value)

def is_hexagonal(N):
    # H_n = n(2n-1) => 2n^2 - n - N = 0
    # n = (1 + math.sqrt(1 + 4*2*N)) / 2(2)
    value = (1 + sqrt(1 + 4*2*N)) / 4
    return value == int(value)

def triangle_number(n):
    return int((n * (n + 1)) / 2)

def find_triangle_pentagonal_hexagonal_number(n):
    found_next = False
    while not found_next:
        T_n = triangle_number(n)
        if is_pentagonal(T_n) and is_hexagonal(T_n):
            return T_n
        n += 1

# Find the next number: T(285) = P(165) = H(143)
next_n = 286
def solve():
    print("The next triangular number that is pentagonal and hexagonal is: %d" % find_triangle_pentagonal_hexagonal_number(next_n))

if __name__ == '__main__':
    solve()
