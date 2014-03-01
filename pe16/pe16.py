# Project Euler Problem 16
# Power digit sum 2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^(1000)?

import time

def timer(*f):
  start = time.time()
  func = f[0]
  args = f[1:]
  return_value = func(*args)
  exec_time = time.time() - start
  print "Execution of function %s in %f seconds with return value: %d" % (func.func_name, exec_time, return_value)

def power_digit_sum(a, b):
  n = a ** b
  s = 0
  while (n):
    d = n % 10
    n = n / 10
    s += d

  return s

def test_power_digit_sum():
  assert(power_digit_sum(2, 15) == 26)
  assert(power_digit_sum(2, 1) == 2)
  assert(power_digit_sum(2, 5) == 5)
  print "Approach 1 Tests pass"


test_power_digit_sum()
timer(power_digit_sum, 2, 1000)

print "Solution to problem 16: Approach 1: Power Sum of Digits of 2**1000 = %d" % power_digit_sum(2, 1000)

def power_digit_sum_2(a, b):
  return reduce(lambda x, y: x + int(y), list(str(a**b)), 0)

def test_power_digit_sum_2():
  assert(power_digit_sum_2(2, 15) == 26)
  assert(power_digit_sum_2(2, 1) == 2)
  assert(power_digit_sum_2(2, 5) == 5)
  print "Approach 2 Tests pass"

test_power_digit_sum_2()
timer(power_digit_sum_2, 2, 1000)

print "Solution to problem 16: Approach 2: Power Sum of Digits of 2**1000 = %d" % power_digit_sum_2(2, 1000)
