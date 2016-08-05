package main

/*
Number Letter Counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
*/
import "fmt"

func CountNumbersAsWords() int {
	// Vocabulary
	sAnd, sHundred := "and", "hundred"
	sTens := []string{"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}

	// Construct Single Digits
	ones := []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	singleDigits := ones[1:]

	// Construct Double Digits
	teens := []string{"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
	tens := []string{}
	for _, ten := range sTens {
		for _, one := range ones {
			s := ""
			if one == "zero" {
				s = ten
			} else {
				s = ten + one
			}
			tens = append(tens, s)
		}
	}

	doubleDigits := []string{"ten"}
	doubleDigits = append(doubleDigits, teens...)
	doubleDigits = append(doubleDigits, tens...)

	// Construct Triple Digits
	hundreds := []string{}
	for _, digit := range singleDigits {
		s := digit + sHundred
		hundreds = append(hundreds, s)
	}
	hundredsAndOnes := []string{}
	for _, hundred := range hundreds {
		for _, one := range ones {
			s := ""
			if one == "zero" {
				s = hundred
			} else {
				s = hundred + sAnd + one
			}
			hundredsAndOnes = append(hundredsAndOnes, s)
		}
	}
	hundredsAndTens := []string{}
	for _, hundred := range hundreds {
		for _, ten := range doubleDigits {
			s := hundred + sAnd + ten
			hundredsAndTens = append(hundredsAndTens, s)
		}
	}
	tripleDigits := []string{}
	tripleDigits = append(tripleDigits, hundredsAndOnes...)
	tripleDigits = append(tripleDigits, hundredsAndTens...)

	//Construct Quadruple Digits
	quadrupleDigits := []string{"onethousand"}

	allNumbers := []string{}
	allNumbers = append(allNumbers, singleDigits...)
	allNumbers = append(allNumbers, doubleDigits...)
	allNumbers = append(allNumbers, tripleDigits...)
	allNumbers = append(allNumbers, quadrupleDigits...)
	letterCount := 0
	for _, n := range allNumbers {
		letterCount += len(n)
	}

	// All numbers
	fmt.Printf(`
         Length single digits: %d
         Length double digits: %d
         Length triple digits: %d
         Length quadruple digits: %d`, len(singleDigits), len(doubleDigits), len(tripleDigits), len(quadrupleDigits))
	fmt.Println()

	return letterCount
}

func solve() int {
	return CountNumbersAsWords()
}

func main() {
	fmt.Printf("The number of letters in the word representations of the numbers 1 to 1000 (in English, excluding spaces, hyphens) is %d\n", solve())
}
