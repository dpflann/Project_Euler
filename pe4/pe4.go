package main

import (
	"fmt"
	"strconv"
)

/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

func isPalindrome(i int) bool {
	strI := strconv.Itoa(i)
	for i, j := 0, len(strI)-1; i < j; i, j = i+1, j-1 {
		if strI[i] != strI[j] {
			return false
		}
	}
	return true
}

func solve() int {
	max := 0
	for i := 999; i > 99; i-- {
		for j := 999; j > 99; j-- {
			product := i * j
			if isPalindrome(product) && product > max {
				fmt.Println(i, j)
				max = product
			}
		}
	}
	return max
}

func main() {
	fmt.Printf("The largest palindrome made from the product of 2 3-digit numbers is: %d\n", solve())
}
