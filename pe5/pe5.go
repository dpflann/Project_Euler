package main

import (
	"fmt"
	"math"
)

/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

func sieve(limit int) []int {
	primes := []int{}
	list := make([]bool, limit)
	list[0] = true
	list[1] = true
	for i, isprime := range list {
		if !isprime {
			primes = append(primes, i)
			for j := i * i; j < limit; j += i {
				list[j] = true
			}
		}
	}
	return primes
}

func solve(limit int) int {
	result := 1.0
	primes := sieve(limit)
	logLimit := math.Log(float64(limit))
	for _, p := range primes {
		// The exp must be found as the maximum value such that p**x is less than the limit
		// p**x = k ==> x * log(p) = log(k) ==> x = floor( log(k) / log(p))
		exp := math.Floor(logLimit / math.Log(float64(p)))
		result = result * math.Floor(math.Pow(float64(p), exp))
	}
	return int(result)
}

func main() {
	limit := 20
	fmt.Printf("The smallest positive number evenly divisible by all of the numbers from 1 to 20 is %d\n", solve(limit))
}
