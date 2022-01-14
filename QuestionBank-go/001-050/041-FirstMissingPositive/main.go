package main

import (
	"fmt"
	"math"
)

/*
缺失的第一个正数
*/

func firstMissingPositive(nums []int) int {
	// 判断有没有1
	flag := true
	for i := range nums {
		if nums[i] == 1 {
			flag = false
		}
	}
	if flag {
		return 1
	}
	// 保证非负
	for i := 0; i < len(nums); i++ {
		if nums[i] <= 0 || nums[i] > len(nums) {
			nums[i] = 1
		}
	}
	fmt.Printf("1.nums:%v\n", nums)
	// 判断
	for i := 0; i < len(nums); i++ {
		loc := int(math.Abs(float64(nums[i]))) - 1
		if nums[loc] > 0 {
			nums[loc] = -nums[loc]
		}
	}
	fmt.Printf("2.nums:%v\n", nums)
	// 第一个正数的下标+1为结果
	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			return i + 1
		}
	}
	return len(nums) + 1
}

func main() {
	nums := []int{7, 8, 9, 11, 12}
	result := firstMissingPositive(nums)
	fmt.Println("result:", result)

}
