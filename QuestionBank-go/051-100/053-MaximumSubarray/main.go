package main

import "fmt"

func maxSubArray(nums []int) int {
	result, sum := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		if sum < 0 {
			sum = nums[i]
		} else {
			sum += nums[i]
		}
		if result < sum {
			result = sum
		}
	}
	return result
}

func main() {
	nums := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	result := maxSubArray(nums)
	fmt.Printf("result:%v\n", result)
}
