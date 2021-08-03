package main

import "fmt"

/*
两数之和
*/
func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)
	for k, v := range nums {
		preIndex, ok := dict[target-v]
		if ok {
			return []int{preIndex, k}
		} else {
			dict[v] = k
		}
	}
	return []int{}
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println("result:", result)
}
