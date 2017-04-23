package main

import (
	"fmt"
)

/*
 You are given the following information, but you may prefer to do some research for yourself.

 1 Jan 1900 was a Sunday.
 Thirty days has September,
 April, June and November.
 All the rest have thirty-one,
 Saving February alone,
 Which has twenty-eight, rain or shine.
 And on leap years, twenty-nine.
 A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
 How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
*/

func GetDaysInMonth(month, year int) int {
	monthsToDays := map[int]int{
		1:  31,
		3:  31,
		4:  30,
		5:  31,
		6:  30,
		7:  31,
		8:  31,
		9:  30,
		10: 31,
		11: 30,
		12: 31,
	}
	if month == 2 {
		if year%4 == 0 {
			if year%100 == 0 && year%400 != 0 {
				return 28
			}
			return 29
		}
		return 28
	}
	return monthsToDays[month]
}

// for a given month, determine which day of the week it begins
func FirstSundays(startYear, endYear int) int {
	firstsOnSunday := 0
	dayForFirstOfMonth := 1 // which is a Tuesday for 1/1/1901
	for year := startYear; year <= endYear; year++ {
		for month := 1; month <= 12; month++ {
			if dayForFirstOfMonth == 6 {
				firstsOnSunday += 1
			}
			d := GetDaysInMonth(month, year)
			offset := d % 7
			dayForFirstOfMonth = (dayForFirstOfMonth + offset) % 7
		}
	}
	return firstsOnSunday
}

func Solve() int {
	return FirstSundays(1901, 2000)
}

func main() {
	// 1/1/1900 was a monday, this is not a leap year, there are 365 days, 365 % 7 is remainder 1 which is "tuesday"
	// days: m-t-w-th-f-sa-su = 0-1-2-3-4-5-6
	fmt.Println("The total number of months that began on Sundays between 1/1/1901 and 12/31/200 is", Solve())
}
