package main

/*
搜索旋转排序数组
*/

func search(nums []int, target int) int {
	for start, end := 0, len(nums)-1; start <= end; {
		mid := (start + end) / 2
		if nums[mid] == target {
			return mid
			// 左半部分有序
		} else if nums[start] <= nums[mid] {
			if nums[start] <= target && target < nums[mid] {
				end = mid - 1
			} else {
				start = mid + 1
			}
			// 右半部分有序
		} else {
			if nums[mid] < target && target <= nums[end] {
				start = mid + 1
			} else {
				end = mid - 1
			}
		}
	}
	return -1
}

func main() {
	nums := []int{4, 5, 6, 7, 0, 1, 2}
	target := 0
	result := search(nums, target)
	println("result:", result)
}
