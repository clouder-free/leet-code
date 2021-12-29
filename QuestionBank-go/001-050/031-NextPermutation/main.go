package main

import "fmt"

/*
下一个排列
*/

func nextPermutation(nums []int) {
	if len(nums) <= 1 {
		return
	}
	// 从右到左 第一个降序的地方
	i := len(nums) - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i -= 1
	}
	if i >= 0 {
		// 从右到左 第一个比nums[i]大的值
		j := len(nums) - 1
		for j > i && nums[j] <= nums[i] {
			j -= 1
		}
		nums[i], nums[j] = nums[j], nums[i]
	}
	// 逆序i+1之后的元素
	for m, n := i+1, len(nums)-1; m < n; {
		nums[m], nums[n] = nums[n], nums[m]
		m += 1
		n -= 1
	}
	fmt.Printf("after:%v\n", nums)
}

func main() {
	nums := []int{1, 2, 3}
	nextPermutation(nums)
	fmt.Printf("before:%v\n", nums)
}
