# How many words in the accompnying txt file have a sum of characters (value based upon alphabetical position) that is a triangle number?

with open('p042_words.txt', 'r') as words_txt:
  words = [w.replace('"', '') for w in words_txt.read().split(',')]

def construct_n_triangle_numbers(n):
  return [int(.5 * i * (i + 1)) for i in range(1, n +1)]

def convert_to_position(c):
  return ord(c) - ord('A') + 1

def calculate_value(word):
  return sum(map(convert_to_position, word))

def solve():
  triangular_numbers = construct_n_triangle_numbers(100)
  triangular_words = [w for w in words if calculate_value(w) in triangular_numbers]
  print('The number of "triangular words" is: %d' % len(triangular_words))

if __name__ == '__main__':
  solve()
