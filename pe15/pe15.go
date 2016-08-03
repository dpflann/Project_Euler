package main

import (
	"fmt"
	"math/big"
)

func paths(r, c *big.Int) *big.Int {
	num, denom, res := new(big.Int), new(big.Int), new(big.Int)
	num.Add(r, c)
	num.Set(factorial(num))
	denom.Mul(factorial(r), factorial(c))
	res.Div(num, denom)
	return res
}

func factorial(n *big.Int) *big.Int {
	result := big.NewInt(1)
	for i := big.NewInt(2); i.Cmp(n) <= 0; i.Add(i, big.NewInt(1)) {
		result.Mul(result, i)
	}
	return result
}

func main() {
	r, c := big.NewInt(int64(20)), big.NewInt(int64(20))
	fmt.Printf("The number of paths that exist from the top-left corner to the bottom-right corner in a 20x20 grid is %s\n", paths(r, c))
}
