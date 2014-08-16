# Find the sum of the digits in the number 100!
import math

def sumDigitsInFactorial(n):
  number = math.factorial(n)
  numberAsString= str(number)
  sumTotal = 0
  for d in numberAsString:
    sumTotal = sumTotal + int(d)
  return sumTotal

def sDiF(n):
  return reduce(lambda x, y: int(x) + int(y), str(math.factorial(n)), 0 )

# factor out all


#####################
def solve():
  print("The sum of the digits in the number 100! is %d." % sumDigitsInFactorial( 100 ))
  print("The sum of the digits in the number 100! is %d." % sDiF( 100 ))


solve()
