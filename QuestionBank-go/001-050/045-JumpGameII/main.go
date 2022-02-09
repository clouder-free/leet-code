package main

import "fmt"

func jump(nums []int) int {
	pos, end, step := 0, 0, 0
	for i := 0; i < len(nums)-1; i++ {
		if pos >= i {
			if pos < i+nums[i] {
				pos = i + nums[i]
			}
			if i == end {
				end = pos
				step += 1
			}
		}
	}
	return step
}

func main() {
	nums := []int{2, 3, 1, 4}
	result := jump(nums)
	fmt.Printf("result:%d\n", result)
}
