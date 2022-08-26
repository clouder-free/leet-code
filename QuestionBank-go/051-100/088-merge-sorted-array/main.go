package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	fmt.Printf("before nums1: %v nums2: %v", nums1, nums2)
	if n == 0 {
		return
	}
	i, j := 0, 0
	for ; i < m && j < n; i += 1 {
		// nums2 j insert nums1 i
		if nums1[i] > nums2[j] {
			// move nums1 backward 1
			for k := m; k > i; k-- {
				nums1[k] = nums1[k-1]
			}
			// insert nums2 j
			nums1[i] = nums2[j]
			// nums2 forward 1
			j += 1
			// nums1 length+1
			m += 1
		}
	}
	for ; j < n; j += 1 {
		nums1[m] = nums2[j]
		m += 1
	}
	fmt.Printf("nums1: %v", nums1)
}

func main() {
	nums1 := []int{1, 2, 3, 0, 0, 0}
	nums2 := []int{2, 5, 6}
	merge(nums1, 3, nums2, 3)
}
