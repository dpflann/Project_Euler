import math
import itertools
import sys
from collections import defaultdict

def extract_anagram_pairs_from_file(word_file='p098_words.txt'):
  with open(word_file, 'r') as f:
    words = f.read().split(',')
    words = [w.strip('"') for w in words]
  return extract_anagram_pairs(words)

def extract_anagram_pairs(words):
  anagrams = defaultdict(list)
  for w in words:
    _hash = tuple(sorted(w))
    anagrams[_hash].append(w)
  anagrams = [ans for ans in anagrams.values() if len(ans) > 1]
  anagram_pairs = []
  for ans in anagrams:
    if len(ans) > 2:
      for w_1, w_2 in itertools.combinations(ans, 2):
        anagram_pairs.append([w_1, w_2])
    else:
      anagram_pairs.append(ans)
  return anagram_pairs

def find_max_mapping_for_word_pair(word_1, word_2):
  _max_square = 0
  _max_mapping = None
  letters = sorted(set(word_1))
  if len(letters) > 10:
    return None
  for p in itertools.permutations('0123456789', len(letters)):
    letter_map = {letters[i]: p[i] for i in range(len(letters))}
    value_1 = apply_letter_map(word_1, letter_map)
    if value_1 == -1 or not is_square(value_1):
      continue
    value_2 = apply_letter_map(word_2, letter_map)
    if value_2 == -1 or not is_square(value_2):
      continue
    max_value = max(value_1, value_2)
    if max_value > _max_square:
      _max_square = max_value
      _max_mapping = letter_map

  return {'words': [word_1, word_2], 'max_square': _max_square, 'max_mapping': _max_mapping}

def apply_letter_map(word, letter_map):
  application = [letter_map[l] for l in word]
  if application[0] == '0':
    return -1
  return int(''.join(application))

def is_square(value):
  return int(math.ceil(math.sqrt(value))) == math.sqrt(value)

def find_max_anagramic_square():
  anagram_pairs = extract_anagram_pairs_from_file()
  max_mappings = [find_max_mapping_for_word_pair(*ans) for ans in anagram_pairs]
  max_mapping = max(max_mappings, key=lambda m: m.get('max_square'))
  return max_mapping

def solve():
  print("The largest square number formed by any member of such a pair of anagrams from the provided file is %d" % find_max_anagramic_square().get('max_square'))


## APPROACH 2

def find_max_square():
  anagram_pairs = extract_anagram_pairs_from_file()
  anagram_pairs_lengths_dict = defaultdict(list)
  for pair in anagram_pairs:
    anagram_pairs_lengths_dict[len(pair[0])].append(pair)
  # Preprocessed to determine the max integer to use as the square based upon
  # the length of the square and the maximum length anagram pair.
  LIMIT = 31623
  for i in range(LIMIT, -1, -1):
    square = i**2
    square_length = len(str(square))
    candidate_anagram_pairs = anagram_pairs_lengths_dict[square_length]
    for w_1, w_2 in candidate_anagram_pairs:
      if len(set(str(square))) != len(set(w_1)):
        continue
      letter_map = {letter:digit for letter, digit in set(zip(w_1, str(square)))}
      w_2_square_str = ''.join([letter_map[l] for l in w_2])
      if w_2_square_str[0] == '0':
        continue
      w_2_square_int = int(w_2_square_str)
      w_2_sqrt = math.sqrt(w_2_square_int)
      if math.floor(w_2_sqrt) == w_2_sqrt:
        return max(square, w_2_square_int)

def solve_2():
  print("The largest square number formed by any member of such a pair of anagrams from the provided file is %d" % find_max_square())

if __name__ == '__main__':
  if len(sys.argv) == 2:
    solution_choice = sys.argv[1]
    if solution_choice == '1':
      solve()
    elif solution_choice == '2':
      solve_2()
  else:
    solve_2()
