package main

import (
	"fmt"
	"sort"
)

/*
三数之和
*/

func threeSum(nums []int) [][]int {
	// 排序
	sort.Ints(nums)
	// fmt.Printf("nums:%v\n", nums)

	result := [][]int{}
	// 开始循环
	for i := 0; i < len(nums); {
		for j, k := i+1, len(nums)-1; j < k; {
			sum := nums[i] + nums[j] + nums[k]
			// fmt.Println("i:", i, "j:", j, "k:", k, "sum:", sum)
			if sum == 0 {
				result = append(result, []int{nums[i], nums[j], nums[k]})
				for j += 1; j < k && nums[j] == nums[j-1]; j += 1 {
				}
				for k -= 1; j < k && nums[k] == nums[k+1]; k -= 1 {
				}
			} else if sum < 0 {
				for j += 1; j < k && nums[j] == nums[j-1]; j += 1 {
				}
			} else {
				for k -= 1; j < k && nums[k] == nums[k+1]; k -= 1 {
				}
			}
		}
		// 移动i
		for i += 1; i < len(nums) && nums[i] == nums[i-1]; i += 1 {
		}
	}
	return result
}

func main() {
	// nums := []int{-1, 0, 1, 2, -1, -4}
	// nums := []int{}
	nums := []int{0}
	result := threeSum(nums)
	fmt.Printf("result:%v\n", result)
}

/*
组成a+b+c=0 三元组
*/
