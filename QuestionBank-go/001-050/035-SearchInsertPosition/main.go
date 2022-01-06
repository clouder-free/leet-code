package main

import "fmt"

/*
搜索插入位置
*/

func searchInsert(nums []int, target int) int {
	if target < nums[0] {
		return 0
	}
	if target > nums[len(nums)-1] {
		return len(nums)
	}
	start, end := 0, len(nums)-1
	for start <= end {
		mid := (start + end) / 2
		if target == nums[mid] {
			return mid
		} else if target > nums[mid] {
			start = mid + 1
		} else {
			end = mid - 1
		}
	}
	return start
}

func main() {
	nums := []int{1, 3, 5, 7, 8}
	target := 6
	result := searchInsert(nums, target)
	fmt.Println("result:", result)
}
