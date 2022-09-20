package main

import "fmt"

func longestConsecutive(nums []int) int {
	numMap := make(map[int]int)
	var result int
	for i := 0; i < len(nums); i++ {
		if numMap[nums[i]] == 0 {
			numMap[nums[i]] = 1
			// current max, min value
			max, min := nums[i], nums[i]-1
			var count int
			for numMap[max] != 0 {
				count += 1
				max += 1
			}
			max -= 1
			for numMap[min] != 0 {
				count += 1
				min -= 1
			}
			min += 1
			numMap[max], numMap[min] = count, count
			if result < count {
				result = count
			}
		}
		fmt.Printf("value:%v numMap:%v\n", nums[i], numMap)
	}
	return result
}

func main() {
	nums := []int{100, 4, 200, 1, 2, 3}
	result := longestConsecutive(nums)
	fmt.Printf("result:%v\n", result)
}
