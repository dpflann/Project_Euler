import string
import random
import math

with open('/usr/share/dict/words', 'r') as f:
    english_words = [w.lower() for w in f.read().split('\n')]

def decrypt():
    with open('p059_cipher.txt', 'r') as f:
        ciphered_ascii = f.read()
    candidates = []
    ciphered_ascii = [int(c) for c in ciphered_ascii.strip('\n').split(',')]
    _max_word_score = 0
    best_candidate = None
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                password = [ord(a), ord(b), ord(c)]
                repeated_password = password * sum(divmod(len(ciphered_ascii), 3)) 
                padded = zip(ciphered_ascii, repeated_password)
                ascii_bytes = [ca ^ rp for ca, rp in padded]
                decoded_ascii = ''.join([chr(c) for c in ascii_bytes])
                word_score = sum([(1 if w.lower() in english_words else 0) for w in decoded_ascii.split(' ')])
                if word_score > _max_word_score:
                    _max_word_score = word_score
                    bytes_sum = sum(ascii_bytes)
                    candidates.append((decoded_ascii, bytes_sum))
                    best_candidate = (decoded_ascii, bytes_sum)
    return best_candidate, candidates

def solve():
    best_candidate, candidates = decrypt()
    print("The sum of the ASCII characters in the original message is: %d" % best_candidate[1])
 
