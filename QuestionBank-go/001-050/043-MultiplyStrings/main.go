package main

import (
	"fmt"
	"strconv"
)

/*
字符串相乘
*/

func multiply(num1 string, num2 string) string {
	//numberMap := map[string]int{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
	//var number1, number2 int
	number1, _ := strconv.Atoi(num1)
	number2, _ := strconv.Atoi(num2)
	for _, n := range num1 {
		v, _ := strconv.Atoi(string(n))
		number1 = number1*10 + v
	}
	for _, n := range num2 {
		v, _ := strconv.Atoi(string(n))
		number2 = number2*10 + v
	}
	return strconv.Itoa(number1 * number2)
}

func main() {
	num1, num2 := "123", "456"
	result := multiply(num1, num2)
	fmt.Println("result:", result)
}
