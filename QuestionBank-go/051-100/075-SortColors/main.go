package main

import "fmt"

func sortColors(nums []int) {
	// 三路快排
	l, r := 0, len(nums)-1
	for i := 0; i <= r; {
		if nums[i] == 0 {
			nums[i], nums[l] = nums[l], nums[i]
			i += 1
			l += 1
		} else if nums[i] == 1 {
			i += 1
		} else {
			nums[i], nums[r] = nums[r], nums[i]
			r -= 1
		}
	}
	fmt.Println("nums:", nums)

}

func main() {
	nums := []int{2, 0, 2, 1, 1, 0}
	fmt.Println("nums:", nums)
	sortColors(nums)
}
