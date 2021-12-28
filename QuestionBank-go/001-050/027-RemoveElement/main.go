package main

/*
移除元素
*/

func removeElement(nums []int, val int) int {
	i := 0
	for j := 0; j < len(nums); j += 1 {
		if nums[j] != val {
			nums[i] = nums[j]
			i += 1
		}
	}
	return i
}

func main() {
	// nums := []int{3, 2, 2, 3}
	nums := []int{0, 1, 2, 2, 3, 0, 4, 2}
	val := 2
	result := removeElement(nums, val)
	println("result:", result)
}
