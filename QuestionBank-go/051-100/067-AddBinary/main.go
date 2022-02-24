package main

import (
	"fmt"
	"strconv"
)

func addBinary(a string, b string) string {
	var flag int
	var result string
	for i := 1; i <= len(a) || i <= len(b); i++ {
		var aVal, bVal int
		if i <= len(a) && a[len(a)-i] == '1' {
			aVal = 1
		}
		if i <= len(b) && b[len(b)-i] == '1' {
			bVal = 1
		}
		value := aVal + bVal + flag
		result = strconv.Itoa(value%2) + result
		flag = value / 2
		//fmt.Printf("%d\n", a[len(a)-i])
	}
	if flag == 1 {
		result = "1" + result
	}
	//fmt.Printf("v:%d, s:%b \n", v, s)
	return result
}

func main() {
	a, b := "11", "1"
	result := addBinary(a, b)
	fmt.Println("result:", result)
}
