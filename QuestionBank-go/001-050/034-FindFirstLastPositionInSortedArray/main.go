package main

import "fmt"

/*
在排序数组中查找元素的第一个和最后一个元素
*/

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	if len(nums) == 1 && nums[0] == target {
		return []int{0, 0}
	}
	result := []int{-1, -1}
	for start, end := 0, len(nums)-1; start <= end; {
		mid := (start + end) / 2
		if nums[mid] == target {
			// 左半部分
			l, r := start, mid
			for l <= r {
				m := (l + r) / 2
				if nums[m] == target {
					result[0] = m
					r = m - 1
				} else {
					l = m + 1
				}
			}
			// 右半部分
			l, r = mid, end
			for l <= r {
				m := (l + r) / 2
				if nums[m] == target {
					result[1] = m
					l = m + 1
				} else {
					r = m - 1
				}
			}
			break
		} else if nums[mid] > target {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}
	return result
}

func main() {
	nums := []int{5, 7, 7, 8, 8, 10}
	target := 7
	result := searchRange(nums, target)
	fmt.Printf("result:%v\n", result)
}
