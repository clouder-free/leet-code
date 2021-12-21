package main

import (
	"math"
	"sort"
)

/*
最接近的三数之和
*/

func threeSumClosest(nums []int, target int) int {
	// 排序
	sort.Ints(nums)
	// fmt.Printf("%v\n", nums)

	result := nums[0] + nums[1] + nums[2]
	for i := 0; i < len(nums); {
		for j, k := i+1, len(nums)-1; j < k; {
			sum := nums[i] + nums[j] + nums[k]
			// fmt.Println("i:", i, "j:", j, "k:", k, "result:", result, "sum:", sum, "target:", target)
			if math.Abs(float64(result-target)) >= math.Abs(float64(sum-target)) {
				result = sum
			}
			if sum-target > 0 {
				for k -= 1; j < k && nums[k] == nums[k+1]; k -= 1 {
				}
			} else if sum-target < 0 {
				for j += 1; j < k && nums[j] == nums[j-1]; j += 1 {
				}
			} else {
				return result
			}
		}
		for i += 1; i < len(nums) && nums[i] == nums[i-1]; i += 1 {
		}
	}
	return result
}

func main() {
	// nums := []int{-1, 2, 1, -4}
	nums := []int{1, 2, 4, 8, 16, 32, 64, 128}
	target := 82
	result := threeSumClosest(nums, target)
	println("result:", result)
}
