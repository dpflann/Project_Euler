package main

import "fmt"

/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

func sumOfMultiples() int {
	sum := 0
	ints := map[int]struct{}{}
	for i := 1; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			_, ok := ints[i]
			if !ok {
				ints[i] = struct{}{}
				sum += i
			}
		}
	}
	return sum
}

func main() {
	fmt.Printf("The sum of all the multiples of 3 or 5 below 1000 is %d.\n", sumOfMultiples())
}
