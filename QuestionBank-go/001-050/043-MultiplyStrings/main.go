package main

import (
	"fmt"
	"strconv"
)

/*
字符串相乘
*/

func multiply(num1 string, num2 string) string {
	////numberMap := map[string]int{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
	////var number1, number2 int
	//number1, _ := strconv.Atoi(num1)
	//number2, _ := strconv.Atoi(num2)
	//for _, n := range num1 {
	//	v, _ := strconv.Atoi(string(n))
	//	number1 = number1*10 + v
	//}
	//for _, n := range num2 {
	//	v, _ := strconv.Atoi(string(n))
	//	number2 = number2*10 + v
	//}
	//return strconv.Itoa(number1 * number2)
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	arr := make([]int, len(num1)+len(num2))
	for i := len(num2) - 1; i >= 0; i-- {
		n2 := int(num2[i] - '0')
		for j := len(num1) - 1; j >= 0; j-- {
			n1 := int(num1[j] - '0')
			sum := n1*n2 + arr[i+j+1]
			arr[i+j+1] = sum % 10
			arr[i+j] += sum / 10
		}
	}
	result := ""
	for i := len(arr) - 1; i >= 0; i-- {
		if i == 0 && arr[i] == 0 {
			break
		}
		result = strconv.Itoa(arr[i]) + result
	}
	return result
}

func main() {
	num1, num2 := "123", "456"
	result := multiply(num1, num2)
	fmt.Println("result:", result)
}
