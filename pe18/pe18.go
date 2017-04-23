package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
 Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                           75
                         95 64
                       17 47 82
                     18 35 87 10
                   20 04 82 47 65
                 19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
             41 41 26 56 83 40 80 70 33
           41 48 72 33 47 32 37 16 94 29
         53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

 NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing
 one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

*/


func ConstructRowTriangle(triangleStr string) [][]int {
	var triangleNumber = 15 // this known from observing the data...
	// construct the triangle numbers as slice of slices
	triangle := make([][]int, triangleNumber)
	allValues := strings.Split(triangleStr, " ")
	currentOffset := 0
	for i := 1; i <= triangleNumber; i++ {
		rowValues := make([]int, i)
		for rvi, j := 0, currentOffset; j < currentOffset+i; j++ {
			rowValues[rvi], _ = strconv.Atoi(allValues[j])
			rvi++
		}
		currentOffset = currentOffset + i
		triangle[i-1] = rowValues
	}
	return triangle
}

func CalculateMaximumPathLength(triangle [][]int) int {
	// begin one row up from the bottom
	for i := len(triangle) - 2; i >= 0; i-- {
		// move through each item in the row, taking the items below it to the left and to the right, and add self, taking the max and storing it as self
		lenTriangleAtI := len(triangle[i])
		for j := 0; j < lenTriangleAtI; j++ {
			sumLeft := triangle[i][j] + triangle[i+1][j]
			sumRight := triangle[i][j] + triangle[i+1][j+1]
			if sumLeft > sumRight {
				triangle[i][j] = sumLeft
			} else {
				triangle[i][j] = sumRight
			}
		}
	}
	return triangle[0][0]
}

func Solve() int {
	var vertices = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

	triangle := ConstructRowTriangle(vertices)
	return CalculateMaximumPathLength(triangle)
}

func main() {
	fmt.Println("The length of the longest path starting from the top is", Solve())
}
