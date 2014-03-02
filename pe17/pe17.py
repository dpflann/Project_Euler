# Project Euler Problem 17

#Number Letter Counts
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def number_letter_counts():
  """Obtain sum of letters used to express numbers form 1 to n,
   ignoring spaces and hyphens, 'and' is part of the number"""
  return construct_letter_numbers()


def construct_letter_numbers():
  # Vocabulary
  sAnd, sHundred, sThousand  = "and", "hundred", "thousand"
  sTens = [ "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
  # Construct Single Digits
  ones = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
  single_digits = ones[1:]
  # Construct Double Digits
  teens = [ "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
  tens = [ ten + one if one != "zero" else ten for ten in sTens for one in ones ]
  double_digits = [ "ten" ] + teens + tens
  # Construct Triple Digits
  hundreds = [ one + sHundred for one in single_digits ]
  hundreds_and_ones = [ hundred + sAnd + one if one != "zero" else hundred for hundred in hundreds for one in ones ]
  hundreds_and_tens = [ hundred + sAnd + ten for hundred in hundreds for ten in double_digits ]
  triple_digits = hundreds_and_ones + hundreds_and_tens
  # Construct Quadruple Digits
  quadruple_digits = [ "onethousand" ]

  # All numbers
  all_numbers = single_digits + double_digits + triple_digits + quadruple_digits
  print """
         Length single digits: %d
         Length double digits: %d
         Length triple digits: %d
         Length quadruple digits: %d
         Length all numbers: %d\n""" % (len(single_digits), len(double_digits), len(triple_digits), len(quadruple_digits), len(all_numbers))

  letter_count = reduce(lambda _sum, n: _sum + len(n), all_numbers, 0)

  return letter_count


print "Number of letters in word representation of number 1 to 1000: %d" % number_letter_counts()

