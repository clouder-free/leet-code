package main

import "fmt"

func subsets(nums []int) [][]int {
	// 初始化
	result := [][]int{{}}
	for i := 0; i < len(nums); i++ {
		for j := range result {
			temp := make([]int, len(result[j]))
			copy(temp, result[j])
			temp = append(temp, nums[i])
			result = append(result, temp)
		}
		fmt.Println("nums[i]:", nums[i], "result:", result)
	}
	return result
}

func main() {
	//nums := []int{1, 2, 3}
	//nums := []int{1, 2, 3, 4}
	nums := []int{9, 0, 3, 5, 7}
	res := subsets(nums)
	fmt.Println(res)
	fmt.Println(len(res))
}
