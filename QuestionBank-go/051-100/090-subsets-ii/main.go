package main

import (
	"fmt"
	"sort"
)

func subsetsWithDup(nums []int) [][]int {
	result := [][]int{{}}
	if len(nums) == 0 {
		return result
	}
	// sort numbers
	sort.Ints(nums)
	// fmt.Printf("nums:%v\n", nums)
	last, size := nums[0], len(result)
	for i := 0; i < len(nums); i++ {
		if last != nums[i] {
			last = nums[i]
			size = len(result)
		}
		temps := [][]int{}
		for start := len(result) - size; start < len(result); start++ {
			temp := make([]int, len(result[start]))
			copy(temp, result[start])
			temps = append(temps, append(temp, nums[i]))
		}
		result = append(result, temps...)
		// fmt.Printf("nums[%v]:%v result:%v\n", i, nums[i], result)
	}
	return result
}

func main() {
	nums := []int{2, 1, 2, 1, 3}
	result := subsetsWithDup(nums)
	fmt.Printf("result:%v\n", result)

}
