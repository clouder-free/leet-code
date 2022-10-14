package main

import (
	"fmt"
	"sort"
)

func singleNumber(nums []int) int {
	sort.Ints(nums)
	var i int
	for i < len(nums)-1 {
		if nums[i] == nums[i+1] && nums[i+1] == nums[i+2] {
			i += 3
		} else {
			return nums[i]
		}
	}
	return nums[i]
}

func main() {
	nums := []int{2, 2, 3, 2}
	result := singleNumber(nums)
	fmt.Printf("result:%v\n", result)
}
