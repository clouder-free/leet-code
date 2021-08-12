package main

import (
	"fmt"
	"strings"
)

/*
Z字型变换
*/

func convert(s string, numRows int) string {
	if s == "" || numRows == 1 {
		return s
	}
	res := make([]string, numRows)
	index, direction := 0, -1
	for i := range s {
		res[index] += string(s[i])
		if index == 0 || index == numRows-1 {
			direction *= -1
		}
		index += direction
	}
	fmt.Printf("res:%v\n", res)
	return strings.Join(res, "")
}

func main() {
	s := "PAYPALISHIRING"
	numRows := 1
	result := convert(s, numRows)
	println("result:", result)
}
