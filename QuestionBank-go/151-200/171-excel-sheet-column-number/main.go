package main

import "fmt"

var titleMap = map[string]int{
	"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
	"K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
	"T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26,
}

func titleToNumber(columnTitle string) int {
	if columnTitle == "" {
		return 0
	}
	if c, ok := titleMap[columnTitle]; ok {
		return c
	}
	return titleToNumber(columnTitle[:len(columnTitle)-1])*26 + titleMap[columnTitle[len(columnTitle)-1:]]
}

func main() {
	columnTitle := "ZY"
	result := titleToNumber(columnTitle)
	fmt.Printf("result:%d\n", result)
}
