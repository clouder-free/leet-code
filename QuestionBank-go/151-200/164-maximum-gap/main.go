package main

import "fmt"

type Pair struct {
	Max int
	Min int
}

func maximumGap(nums []int) int {
	if len(nums) < 2 {
		return 0
	}
	// max min value
	max, min := nums[0], nums[0]
	for _, n := range nums {
		if n < min {
			min = n
		}
		if n > max {
			max = n
		}
	}
	// bucket size
	size := 1
	if (max-min)/(len(nums)-1) > size {
		size = (max - min) / (len(nums) - 1)
	}
	// bucket number
	number := (max-min)/size + 1
	buckets := make([]Pair, number)
	// bucket init
	for i := range buckets {
		buckets[i] = Pair{-1, -1}
	}
	for _, n := range nums {
		bucketIndex := (n - min) / size
		if buckets[bucketIndex].Max == -1 {
			buckets[bucketIndex].Min = n
			buckets[bucketIndex].Max = n
		} else {
			if buckets[bucketIndex].Min > n {
				buckets[bucketIndex].Min = n
			}
			if buckets[bucketIndex].Max < n {
				buckets[bucketIndex].Max = n
			}
		}
	}
	fmt.Printf("%v\n", buckets)
	// max gap
	prev, result := -1, buckets[0].Max-buckets[0].Min
	for i, b := range buckets {
		if b.Min == -1 {
			continue
		}
		if prev != -1 {
			if b.Min-buckets[prev].Max > result {
				result = b.Min - buckets[prev].Max
			}
		}
		prev = i
	}
	return result
}

func main() {
	nums := []int{1, 1, 1, 1}
	result := maximumGap(nums)
	fmt.Printf("%v\n", result)

}
