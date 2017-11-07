#!/usr/bin/python
# -*- coding: utf8 -*-

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# 
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# 
# (Please note that the palindromic number, in either base, may not include leading zeros.)

oneMillion = 10**6

def cleanBinaryFormat(i):
  return bin(i)[2:]

def isPalindromic(s):
  i = 0
  j = len(s) - 1
  while (i < j and s[i] == s[j]):
    i = i + 1
    j = j - 1
  return i >= j

def sumOfPalindromicNumbers(n):
  return sum([ i for i in range(1, n) if isPalindromic(str(i)) and isPalindromic(cleanBinaryFormat(i)) ])

def solve():
  print "The sum of all the numbers, less than one million, which are palindromic in base 10 and base 2 is %d." % sumOfPalindromicNumbers(oneMillion)

if __name__ == '__main__':
  solve()
