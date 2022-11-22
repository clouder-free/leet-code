package main

import "fmt"

func maxProduct(nums []int) int {
	result, min, max := nums[0], nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] < 0 {
			min, max = max, min
		}
		if nums[i] < max*nums[i] {
			max = max * nums[i]
		} else {
			max = nums[i]
		}
		if nums[i] > min*nums[i] {
			min = min * nums[i]
		} else {
			min = nums[i]
		}
		if result < max {
			result = max
		}
	}
	return result
}

func main() {
	nums := []int{2, 3, -2, 4}
	result := maxProduct(nums)
	fmt.Printf("%v\n", result)
}
