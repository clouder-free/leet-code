package main

import "fmt"

/*
删除有序数组中的重复项
*/

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	count := 0
	for i := 1; i < len(nums); i += 1 {
		if nums[i] != nums[count] {
			count += 1
			nums[count] = nums[i]
		}
	}
	fmt.Printf("%v\n", nums)
	return count + 1
}

func main() {
	// nums := []int{1, 1, 2}
	nums := []int{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}
	fmt.Printf("%v\n", nums)
	result := removeDuplicates(nums)
	fmt.Println("result:", result)
}
