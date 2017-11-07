#!/usr/bin/python
# -*- coding: utf8 -*-

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# a = sqrt(c**2 - b**2)
# b = sqrt(c**2 - a**2)
# c = sqrt(a**2 + b**2)
# a = p - b - c
# b = p - a - c
# c = p - a - b
# 
# (p - a - b)**2  = a**2 + b**2
# p**2 - pa - pb - pa + a**2 + ab - pb + ab + b**2 = a**2 + b**2
# p**2 - 2pa - 2pb + 2ab + a**2 + b**2 = a**2 + b**2
# p**2 - 2pa - 2pb + 2ab = 0
# p**2 = 2pa + 2pb - 2ab
# p**2 = 2pa - 2ab + 2pb
# p**2 - 2pa = 2pb - 2ab
# (p**2 - 2pa) = 2b(p - a)
# (p**2 - 2pa)/(p - a)/2 = b

def find_triangular_integral_sides(p):
  integral_sides = set()
  p_2 = p**2
  for a in range(1, p):
    b = (p_2 - 2*p*a) / (p - a) / 2
    c = p - a - b
    sides = map(int, [a, b, c])
    if any(map(lambda s: s <= 0, sides)):
      continue
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
      integral_sides.add(tuple(sorted(sides)))
  return integral_sides

def find_maximum_perimeter(limit):
  perimeter_sides_dict = []
  for p in range(1, limit + 1):
    perimeter_sides_dict.append((p, len(find_triangular_integral_sides(p))))
  return max(perimeter_sides_dict, key=lambda t: t[1])

def solve(limit=1000):
  print "The p <= 1000 for which the number of integral-side, right-angle triangles is maximized is %d." % find_maximum_perimeter(limit)[0]

if __name__ == '__main__':
  solve()
