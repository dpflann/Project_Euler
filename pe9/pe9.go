package main

import (
	"fmt"
)

/*
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = ^25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
*/

func constraints(a, b int, goal int) (int, bool) {
	aSquared := a * a
	bSquared := b * b
	c := goal - a - b
	if (a < b && b < c) && c*c == aSquared+bSquared {
		return c, true
	}
	return c, false
}

func solve(goal int) int {
	foundC := false
	product := 1
	for a := goal - 1; !foundC && a > 0; a-- {
		for b := goal - 1; !foundC && b > 0; b-- {
			c, foundC := constraints(a, b, goal)
			if foundC {
				fmt.Println(a, b, c)
				return a * b * c
			}
		}
	}
	return product
}

func main() {
	goal := 1000
	fmt.Printf("The product of a*b*c such a + b + c = %d and a^2 + b^2 = c^2 (Pythagorean Triples) is %d\n", goal, solve(goal))
}
