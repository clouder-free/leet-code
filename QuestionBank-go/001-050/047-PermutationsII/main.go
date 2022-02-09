package main

import (
	"fmt"
	"sort"
)

func permuteUnique(nums []int) [][]int {
	// 排序
	sort.Ints(nums)
	//fmt.Printf("%v\n", nums)
	return permute(nums)
}

func permute(nums []int) [][]int {
	var result [][]int
	if len(nums) == 1 {
		result = append(result, nums)
		return result
	}
	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i-1] == nums[i] {
			continue
		}
		var n []int
		n = append(n, nums[:i]...)
		n = append(n, nums[i+1:]...)
		temp := permute(n)
		for j := 0; j < len(temp); j++ {
			r := []int{nums[i]}
			r = append(r, temp[j]...)
			result = append(result, r)
		}
	}
	return result
}

func main() {
	nums := []int{1, 2, 1}
	result := permuteUnique(nums)
	for i := range result {
		fmt.Printf("%v\n", result[i])
	}
}
