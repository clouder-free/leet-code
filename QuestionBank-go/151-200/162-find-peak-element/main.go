package main

func findPeakElement(nums []int) int {
	return peakElement(nums, 0, len(nums)-1)
}

func peakElement(nums []int, start, end int) int {
	if start == end {
		return start
	}
	mid := (start + end) / 2
	if nums[mid] > nums[mid+1] {
		return peakElement(nums, start, mid)
	}
	return peakElement(nums, mid+1, end)
}
