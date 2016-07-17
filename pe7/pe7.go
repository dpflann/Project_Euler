package main

/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

import "fmt"

func nthPrime(n int) int {
	primes := []int{}
	list := make([]bool, 10000000)
	list[0] = true
	list[1] = true
	for i, isprime := range list {
		if !isprime {
			primes = append(primes, i)
			for j := i * i; j < len(list); j += i {
				list[j] = true
			}
		}
		if len(primes) > n {
			return primes[n-1]
		}
	}
	return -1
}

func main() {
	fmt.Printf("The 10,001st prime is %d\n", nthPrime(10001))
}
