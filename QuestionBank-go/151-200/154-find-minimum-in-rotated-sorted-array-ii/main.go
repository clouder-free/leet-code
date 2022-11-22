package main

import "fmt"

func findMin(nums []int) int {
	i, j := 0, len(nums)-1
	for i <= j {
		k := (i + j) / 2
		println("i:", i, "j:", j, "k:", k)
		if nums[k] > nums[j] {
			i = k + 1
		} else if nums[k] < nums[j] {
			j = k
		} else {
			j = j - 1
		}
	}
	return nums[i]
}

func main() {
	nums := []int{3, 1, 1}
	result := findMin(nums)
	fmt.Printf("%v\n", result)
}
