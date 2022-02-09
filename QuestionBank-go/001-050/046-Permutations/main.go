package main

import "fmt"

func permute(nums []int) [][]int {
	var result [][]int
	if len(nums) == 1 {
		result = append(result, nums)
		return result
	}
	for i := 0; i < len(nums); i++ {
		var n []int
		n = append(n, nums[:i]...)
		n = append(n, nums[i+1:]...)
		temp := permute(n)
		for j := 0; j < len(temp); j++ {
			var r []int
			r = append(r, nums[i])
			r = append(r, temp[j]...)
			result = append(result, r)
		}
	}
	return result
}

func main() {
	nums := []int{0, 1}
	result := permute(nums)
	for i := 0; i < len(result); i++ {
		fmt.Printf("%v\n", result[i])
	}
}
