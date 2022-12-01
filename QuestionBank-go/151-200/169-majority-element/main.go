package main

import "fmt"

func majorityElement(nums []int) int {
	countMap := make(map[int]int)
	for _, n := range nums {
		countMap[n] += 1
		if countMap[n] > len(nums)/2 {
			return n
		}
	}
	return -1
}

func main() {
	nums := []int{2, 2, 1, 1, 1, 2, 2}
	result := majorityElement(nums)
	fmt.Printf("result:%d\n", result)

}
