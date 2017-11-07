# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import itertools as it
from fractions import Fraction

def findCuriousFractionsProduct():
    # only considering fractions with two digits in numerator and denominator
    numerators = []
    denominators = []
    ns = range(10, 100)
    fractions = it.product(ns, ns)
    for f in fractions:
        n, d = f
        if (n / d) >= 1:
            continue
        n_1 = n / 10
        n_0 = n % 10
        d_1 = d / 10
        d_0 = d % 10
        if d_0 == 0 or n_0 == 0:
            continue
        operands = (1, 1)
        if n_1 == d_0:
            operands = (n_0, d_1)
        elif n_1 == d_1:
            operands = (n_0, d_0)
        elif n_0 == d_0:
            operands = (n_1, d_1)
        elif n_0 == d_1:
            operands = (n_1, d_0)
        num, den = operands
        if (1.0 * num / den) == (1.0 * n / d):
            numerators.append(num)
            denominators.append(den)
    return Fraction(reduce(lambda x, y: x * y, numerators), reduce(lambda x, y: x * y, denominators))

def solve():
    print "The value of the denominator of the product of the four fraction in lowest common terms is %d." % findCuriousFractionsProduct().denominator 

if __name__ == '__main__':
  solve()
