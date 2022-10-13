package main

import (
	"fmt"
	"sort"
)

func singleNumber(nums []int) int {
	sort.Ints(nums)
	var i int
	for i < len(nums)-1 {
		if nums[i] == nums[i+1] {
			i += 2
		} else {
			return nums[i]
		}
	}
	return nums[i]
}

func main() {
	nums := []int{4, 1, 2, 1, 2}
	result := singleNumber(nums)
	fmt.Printf("result:%v\n", result)
}
