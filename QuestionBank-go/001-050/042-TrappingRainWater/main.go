package main

import "fmt"

/*
接雨水
*/

func trap(height []int) int {
	result := 0
	var stack []int
	for i := 0; i < len(height); i += 1 {
		for len(stack) > 0 && height[stack[len(stack)-1]] < height[i] {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if len(stack) > 0 {
				dis := i - stack[len(stack)-1] - 1
				var h int
				if height[stack[len(stack)-1]] >= height[i] {
					h = height[i] - height[top]
				} else {
					h = height[stack[len(stack)-1]] - height[top]
				}
				result += dis * h
			}
		}
		stack = append(stack, i)
	}

	return result
}

/*
双指针法
*/
func trap2(height []int) int {
	result := 0
	// 第一个柱子和最后一个柱子不接雨水
	for i := 1; i < len(height)-1; i += 1 {
		leftHeight, rightHeight := height[i], height[i]
		for m := i - 1; m >= 0; m -= 1 {
			if height[m] > leftHeight {
				leftHeight = height[m]
			}
		}
		for n := i + 1; n < len(height); n += 1 {
			if height[n] > rightHeight {
				rightHeight = height[n]
			}
		}
		var h int
		if leftHeight <= rightHeight {
			h = leftHeight - height[i]
		} else {
			h = rightHeight - height[i]
		}
		if h > 0 {
			result += h
		}
	}
	return result
}

func trap3(height []int) int {
	// 分配空间 来确定当前最大的高度
	left := make([]int, len(height))
	right := make([]int, len(height))
	current := 0
	for i := 0; i < len(height); i += 1 {
		left[i] = current
		if current < height[i] {
			current = height[i]
		}
	}
	fmt.Println("left:", left)
	current = 0
	for i := len(height) - 1; i >= 0; i -= 1 {
		right[i] = current
		if current < height[i] {
			current = height[i]
		}
	}
	fmt.Println("right:", right)
	result := 0
	for i := 1; i < len(height)-1; i += 1 {
		var h int
		if left[i] > right[i] {
			h = right[i] - height[i]
		} else {
			h = left[i] - height[i]
		}
		if h > 0 {
			result += h
		}
	}
	return result
}

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	result := trap3(height)
	fmt.Println("result:", result)
}
