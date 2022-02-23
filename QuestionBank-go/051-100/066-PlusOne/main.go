package main

import "fmt"

func plusOne(digits []int) []int {
	flag := 1
	for i := len(digits) - 1; i >= 0; i-- {
		digits[i] += flag
		flag = digits[i] / 10
		digits[i] %= 10
	}
	if flag == 1 {
		digits = append(append([]int{}, 1), digits...)
	}
	return digits
}

func main() {
	digits := []int{9, 9, 9}
	result := plusOne(digits)
	fmt.Println("result:", result)
}
