package main

import (
	"fmt"
	"math/big"
)

func PowerDigitSum(a, b *big.Int) *big.Int {
	z := new(big.Int)
	z.Exp(a, b, nil)
	sum := new(big.Int)
	zero := big.NewInt(0)
	ten := big.NewInt(10)
	d := new(big.Int)
	for z.Cmp(zero) > 0 {
		d.Mod(z, ten)
		z.Div(z, ten)
		sum.Add(sum, d)
	}
	return sum
}

func solve(a, b int64) *big.Int {
	return PowerDigitSum(big.NewInt(a), big.NewInt(b))
}

func main() {
	fmt.Printf("The sum of the digits of 2^1000 is %s\n", solve(2, 1000))
}
