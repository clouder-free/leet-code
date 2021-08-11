package main

import "fmt"

/*
寻找两个正序数组的中位数
*/

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	nums := []int{}
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] < nums2[j] {
			nums = append(nums, nums1[i])
			i++
		} else {
			nums = append(nums, nums2[j])
			j++
		}
	}
	if i < len(nums1) {
		nums = append(nums, nums1[i:]...)
	}
	if j < len(nums2) {
		nums = append(nums, nums2[j:]...)
	}
	fmt.Printf("nums: %v\n", nums)
	mid := len(nums) / 2
	println("mid:", mid)
	var result float64
	if len(nums)%2 == 0 {
		result = float64(nums[mid]+nums[mid-1]) / 2.0
	} else {
		result = float64(nums[mid])
	}
	return result
}

func findMedianSortedArrays2(nums1 []int, nums2 []int) float64 {
	i, j := 0, 0
	left, right := 0, 0
	var number int
	mid := (len(nums1) + len(nums2)) / 2
	for i+j <= mid {
		if i < len(nums1) && j < len(nums2) {
			if nums1[i] < nums2[j] {
				number = nums1[i]
				i++
			} else {
				number = nums2[j]
				j++
			}
		} else if i == len(nums1) {
			number = nums2[j]
			j++
		} else if j == len(nums2) {
			number = nums1[i]
			i++
		} else {
			number = 0
		}
		left, right = right, number
	}
	// println("left:", left, "right:", right)
	var result float64
	if (len(nums1)+len(nums2))%2 == 0 {
		result = float64(left+right) / 2.0
	} else {
		result = float64(right)
	}
	return result
}

func main() {
	// nums1 := []int{1, 3}
	// nums2 := []int{2}
	nums1 := []int{1, 2}
	nums2 := []int{3, 4}
	// nums1 := []int{0, 0}
	// nums2 := []int{0, 0}
	// nums1 := []int{}
	// nums2 := []int{2}
	res := findMedianSortedArrays2(nums1, nums2)
	println("result:", res)
}
