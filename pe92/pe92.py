def square_digits(n):
    square_digit_sum = 0
    while n:
        _digit = n % 10
        square_digit_sum += _digit**2
        n = n / 10
    return square_digit_sum

def number_chain(n, chains):
    seen_numbers = []
    next_link = n 
    if next_link in chains:
        return chains[n]
    while next_link not in seen_numbers and next_link != 1 and next_link != 89:
        if next_link in chains:
            for c in chains[next_link]:
                if c not in seen_numbers and c != 1 and c != 89:
                    seen_numbers.append(c)
                else:
                    next_link =  c
                    break
        else:
            seen_numbers.append(next_link)
            next_link = square_digits(next_link)
    seen_numbers.append(next_link)
    chains[n] = seen_numbers
    return seen_numbers

def find_number_chains(limit=10000000):
    chains_dict = {}
    chains = [number_chain(n, chains_dict) for n in range(1, limit+1)]
    chains_ending_in_89 = [c for c in chains if c[-1] == 89]
    return len(chains_ending_in_89), chains, chains_dict 

def solve(limit=10000000):
  n, c, dc = find_number_chains(limit=limit)
  print("The total number of numbers less than %d that will arrive at 89 as 'number chains' is %d" % (limit, n))

if __name__ == '__main__':
  solve()
