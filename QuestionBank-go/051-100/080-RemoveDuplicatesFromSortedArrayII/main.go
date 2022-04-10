package main

import "fmt"

func removeDuplicates(nums []int) int {
	// 元素最多出现K次
	i, j, k := 0, 1, 1
	for ;j < len(nums); {
		if nums[i] == nums[j] {
			if k > 0 {
				nums[i+1] = nums[j]
				i += 1
				k -= 1
			}
		} else {
			nums[i+1] = nums[j]
			i += 1
			k = 1
		}
		j += 1
		//if k > 0 {
		//	i += 1
		//	k -= 1
		//	nums[i] = nums[j]
		//	j += 1
		//	if j<len(nums) && nums[i] != nums[j] {
		//		k = 2
		//	}
		//} else {
		//	if nums[i] != nums[j] {
		//		k = 2
		//	} else {
		//		j += 1
		//	}
		//}
	}
	fmt.Println("nums:", nums)
	return i+1
}

func main() {
	nums := []int{0, 0, 1, 1, 1, 1, 2, 3, 3}
	result := removeDuplicates(nums)
	fmt.Println("result:", result)
}
