package main

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

import (
	"fmt"
)

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
	primes := sieve(limit)
	sum := 0
	for _, p := range primes {
		sum += p
	}
	return sum
}

func main() {
	limit := 2000000
	fmt.Printf("The sum of all the primes below 2 million is %d\n", solve(limit))
}
