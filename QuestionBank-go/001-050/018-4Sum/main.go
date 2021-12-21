package main

import (
	"fmt"
	"sort"
)

/*
四数之和
*/

func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	// fmt.Printf("%v\n", nums)
	result := [][]int{}
	for i := 0; i < len(nums); {
		for j := i + 1; j < len(nums); {
			for m, n := j+1, len(nums)-1; m < n; {
				sum := nums[i] + nums[j] + nums[m] + nums[n]
				if sum == target {
					result = append(result, []int{nums[i], nums[j], nums[m], nums[n]})
					for m += 1; m < n && nums[m] == nums[m-1]; m += 1 {
					}
					for n -= 1; m < n && nums[n] == nums[n+1]; n -= 1 {
					}
				} else if sum > target {
					for n -= 1; m < n && nums[n] == nums[n+1]; n -= 1 {
					}
				} else {
					for m += 1; m < n && nums[m] == nums[m-1]; m += 1 {
					}
				}
			}
			for j += 1; j < len(nums) && nums[j] == nums[j-1]; j += 1 {
			}
		}
		for i += 1; i < len(nums) && nums[i] == nums[i-1]; i += 1 {
		}
	}
	return result
}

func main() {
	// nums := []int{1, 0, -1, 0, -2, 2}
	nums := []int{2, 2, 2, 2}
	target := 8
	result := fourSum(nums, target)
	fmt.Printf("result:%v\n", result)
}
