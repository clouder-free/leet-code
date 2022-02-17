package main

import "fmt"

func canJump(nums []int) bool {
	jump := make([]bool, len(nums))
	for i, j := len(nums)-1, len(nums)-1; i > -1; i-- {
		if nums[i] >= j-i {
			j = i
			jump[i] = true
		}
	}
	return jump[0]
}

func main() {
	//nums := []int{2, 3, 1, 1, 4}
	nums := []int{3, 2, 1, 0, 4}
	result := canJump(nums)
	fmt.Printf("result: %v\n", result)
}
