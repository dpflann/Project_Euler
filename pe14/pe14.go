package main

/*
The following iterative sequence is defined for the set of positive integers:

  n -> n/2 (n is even)
  n -> 3n + 1 (n is odd)

  Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
*/

import "fmt"

func collatz(n int, collatzLengths *map[int]int) int {
	if c, ok := (*collatzLengths)[n]; ok {
		return c
	}
	if n%2 == 0 {
		(*collatzLengths)[n] = 1 + collatz(n/2, collatzLengths)
		return (*collatzLengths)[n]
	} else {
		(*collatzLengths)[n] = 1 + collatz(3*n+1, collatzLengths)
		return (*collatzLengths)[n]
	}
}

func solve(limit int) int {
	collatzLengths := map[int]int{0: 0, 1: 1}
	for i := 0; i <= limit; i++ {
		collatz(i, &collatzLengths)
	}
	maxLength := -1
	longestChainN := 0
	for n, length := range collatzLengths {
		if length > maxLength {
			longestChainN, maxLength = n, length
		}
	}
	return longestChainN
}

func main() {
	limit := 1000000
	fmt.Printf("The number below 1000000 with the longest collatz sequence is %d\n", solve(limit))
}
