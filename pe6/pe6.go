package main

/*
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

import (
	"fmt"
	"math"
)

func solve(limit int) int64 {
	sumOfSquares := 0.0
	squareOfSum := 0.0
	two := float64(2)
	for i := 1; i <= limit; i++ {
		square := math.Pow(float64(i), two)
		sumOfSquares = sumOfSquares + square
		squareOfSum = squareOfSum + float64(i)
	}
	squareOfSum = math.Pow(squareOfSum, two)
	return int64(squareOfSum - sumOfSquares)
}

func main() {
	limit := 100
	fmt.Printf("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is %d\n", solve(limit))
}
