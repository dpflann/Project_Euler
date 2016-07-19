package main

/*
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
d*c = a, 1 <= d <= a, 1 <= c <= a, d inversly proportional to c, only need to test values up to (a^(1/2)), find the first number
with 250 divisors less than (a^(1/2))

What is the value of the first triangle number to have over five hundred divisors?
*/

import "fmt"

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

func primeFactorsAndExponents(n int, primes *[]int) map[int]int {
	primesAndExponents := map[int]int{}
	for _, p := range *primes {
		e := 0
		for n%p == 0 {
			n /= p
			e++
		}
		if e > 0 {
			primesAndExponents[p] = e
		}
	}
	return primesAndExponents
}

// divisors examines the exponents of prime factors and uses the trick that because p_1^(a_1) * p_2^(a_2) * ... = n,
// D(n) = (a_1 + 1)*(a_2 + 1)*... = # of divisors
func divisors(m map[int]int) int {
	d := 1
	for _, v := range m {
		d = d * (v + 1)
	}
	return d
}

func solve(numberOfDivisors, limit int) int {
	primes := sieve(limit)
	n := 1
	for i := 2; divisors(primeFactorsAndExponents(n, &primes)) < numberOfDivisors; i++ {
		n += i
	}
	return n
}

func main() {
	constraint := 500
	primeLimit := 18 // twiddled with to find lower bound on needed primes, significant execution time reduction
	fmt.Printf("The first triangle number to have over 500 divisors is %d.\n", solve(constraint, primeLimit))
}
