package main

import (
	"fmt"
	"math"
)

/*
	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
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

func main() {
	limit := 600851475143
	primes := sieve(int(math.Ceil(math.Sqrt(float64(limit)))))
	lpf := -1
	for i := len(primes) - 1; i > -1; i-- {
		if limit%primes[i] == 0 {
			lpf = primes[i]
			break
		}
	}
	fmt.Printf("The largest prime factor of %d is %d.\n", limit, lpf)
}
