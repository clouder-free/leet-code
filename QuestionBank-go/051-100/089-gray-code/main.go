package main

import "fmt"

func grayCode(n int) []int {
	result := []int{}
	size := 1 << n
	for i := 0; i < size; i++ {
		result = append(result, (i>>1)^i)
	}
	return result
}

func main() {
	result := grayCode(3)
	fmt.Printf("result:%v\n", result)
}
