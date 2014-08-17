# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

import math as m

def digits(n):
    log10n = m.log10(n)
    ceilLog10n = m.ceil(log10n)
    if log10n == ceilLog10n:
        return log10n + 1
    return ceilLog10n

def fibonacci(n):
    phi = ( 1 + m.sqrt(5) ) / 2.0
    return m.floor( ( phi / m.sqrt(5) ) + .5 )

# Fib(n) = [ phi^n / sqrt(5) ] where [ ] = integer closest to
# http://en.wikipedia.org/wiki/Fibonacci_number#Computation_by_rounding
def firstFibWithNdigits(n):
    phi = ( 1 + m.sqrt(5) ) / 2.0
    n = 1
    log10phi = m.log10(phi)
    log10RootFive = m.log10(m.sqrt(5))
    logFib = n * log10phi - log10RootFive

    while ( logFib <= 999 ):
        n = n + 1
        logFib = n * log10phi - log10RootFive

    return n 

# The first function is inefficient
def fFwNd(n):
  phi = ( 1 + m.sqrt(5) ) / 2.0
  log10phi = m.log10(phi)
  log10RootFive = m.log10(m.sqrt(5))
  limit = n - 1
  nth = (limit + log10RootFive) / log10phi
  return m.ceil(nth)

def solve():
    print "The first Fibonacci number to have 1000 digits is %d." % firstFibWithNdigits(1000)
    print "The first Fibonacci number to have 1000 digits is %d." % fFwNd(1000)

