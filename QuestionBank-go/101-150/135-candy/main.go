package main

import "fmt"

func candy(ratings []int) int {
	// init
	left := make([]int, len(ratings))
	right := make([]int, len(ratings))
	total := 0
	for i := 0; i < len(ratings); i++ {
		left[i] = 1
		right[i] = 1
	}
	// left to right
	for i := 1; i < len(ratings); i++ {
		if ratings[i] > ratings[i-1] {
			left[i] = left[i-1] + 1
		}
	}
	// right to left
	for i := len(ratings) - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			right[i] = right[i+1] + 1
		}
		if left[i] > right[i] {
			total += left[i]
		} else {
			total += right[i]
		}
	}
	if left[len(left)-1] > right[len(right)-1] {
		total += left[len(left)-1]
	} else {
		total += right[len(right)-1]
	}
	return total
}

func main() {
	ratings := []int{1, 0, 2}
	result := candy(ratings)
	fmt.Printf("result:%v\n", result)
}
