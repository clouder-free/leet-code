package main

import (
	"fmt"
	"strconv"
)

func evalRPN(tokens []string) int {
	numbers := []int{}
	for i := 0; i < len(tokens); i++ {
		if tokens[i] == "+" {
			n := numbers[len(numbers)-2] + numbers[len(numbers)-1]
			numbers = append(numbers[:len(numbers)-2], n)
		} else if tokens[i] == "-" {
			n := numbers[len(numbers)-2] - numbers[len(numbers)-1]
			numbers = append(numbers[:len(numbers)-2], n)
		} else if tokens[i] == "*" {
			n := numbers[len(numbers)-2] * numbers[len(numbers)-1]
			numbers = append(numbers[:len(numbers)-2], n)
		} else if tokens[i] == "/" {
			n := numbers[len(numbers)-2] / numbers[len(numbers)-1]
			numbers = append(numbers[:len(numbers)-2], n)
		} else {
			n, _ := strconv.Atoi(tokens[i])
			numbers = append(numbers, n)
		}
		fmt.Printf("%v\n", numbers)
	}
	return numbers[0]
}

func main() {
	tokens := []string{"2", "1", "+", "3", "*"}
	result := evalRPN(tokens)
	fmt.Println("result:", result)
}
