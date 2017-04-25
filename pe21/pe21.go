package main

import "fmt"

/*
  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
  If d(a) = b and d(b) = a, where a not equal b, then a and b are an amicable pair and each of a and b are called amicable numbers.

  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
  The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
  Evaluate the sum of all the amicable numbers under 10000.
  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
  If d(a) = b and d(b) = a, where a not equal b, then a and b are an amicable pair and each of a and b are called amicable numbers.

  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
  The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

  Evaluate the sum of all the amicable numbers under 10000.
*/

func SumProperDivisors(n int) int {
	sum := 0
	for i := 1; i < n; i++ {
		if n%i == 0 {
			sum += i
		}
	}
	return sum
}

func FindAmicablePairs(limit int) int {
	sumOfAmicablePairs := 0
	iToSum := make(map[int]int, limit-1)
	for i := 1; i < limit; i++ {
		sum := SumProperDivisors(i)
		iToSum[i] = sum
		if a, ok := iToSum[sum]; ok {
			if a == i && (sum != i) {
				sumOfAmicablePairs += (i + sum)
			}
		}
	}
	return sumOfAmicablePairs
}

func Solve() int {
	limit := 10000
	return FindAmicablePairs(limit)
}

func main() {
	fmt.Println("The sum of all the amicable numbers under 10000 is", Solve())
}
