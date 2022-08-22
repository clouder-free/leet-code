package main

import "fmt"

func search(nums []int, target int) bool {
	l, r := 0, len(nums)-1
	for ;l <= r; {
		m := (l+r)/2
		if nums[m] == target {
			return true
		} else if nums[m] < target {
			if nums[m] < target && target <= nums[r] {
				l = m+1
			} else {
				r = m-1
			}
		} else {
			if nums[l] <= target && target < nums[m] {
				r = m-1
			} else {
				l = m+1
			}
		}
	}
	return false
}

func main() {
	nums := []int{2,5,6,0,0,1,2}
	target := 0
	result := search(nums, target)
	fmt.Println("result: ", result)
}
