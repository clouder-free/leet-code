package main

import "fmt"

func findMin(nums []int) int {
	result := nums[0]
	for i, j := 0, len(nums)-1; i <= j; {
		k := (i + j) / 2
		// 左连续
		if nums[i] <= nums[k] {
			if result > nums[i] {
				result = nums[i]
			}
			i = k + 1
			// 右连续
		} else {
			if result > nums[k] {
				result = nums[k]
			}
			j = k - 1
		}
	}
	return result
}

func main() {
	nums := []int{3, 4, 5, 1, 2}
	result := findMin(nums)
	fmt.Printf("%v\n", result)
}
