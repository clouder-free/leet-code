package main

import "fmt"

func trailingZeroes(n int) int {
	result := 0
	for i := 5; i <= n; i += 5 {
		for j := i; j%5 == 0; j /= 5 {
			result += 1
		}
	}
	return result
}

func main() {
	result := trailingZeroes(25)
	fmt.Printf("result:%d\n", result)
}
