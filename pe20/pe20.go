package main

import (
	"fmt"
	"math/big"
	"strconv"
)

func Solve() int {
	var f big.Int
	f.MulRange(1, 100)
	str := f.String()
	sum := 0
	for i := range str {
		val, _ := strconv.Atoi(string(str[i]))
		sum += val
	}
	return sum
}

func main() {
	fmt.Println("The sum of the digits in the number 100! is", Solve())
}
