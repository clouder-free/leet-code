package main

func largestRectangleArea(heights []int) int {
	var result int
	// 单调递增栈
	var stack []int
	for i := 0; i < len(heights); i++ {
		for len(stack) > 0 && heights[stack[len(stack)-1]] >= heights[i] {
			// pop last element of stack
			h := stack[len(stack)-1]
			stack = append([]int{}, stack[:len(stack)-1]...)
			var width int
			// stack not empty
			if len(stack) > 0 {
				width = i - stack[len(stack)-1] - 1
			} else {
				// stack empty
				width = i
			}
			if result < heights[h]*width {
				result = heights[h] * width
			}
		}
		stack = append(stack, i)
	}
	if len(stack) > 0 {
		last := stack[len(stack)-1]
		for len(stack) > 0 {
			h := stack[len(stack)-1]
			stack = append([]int{}, stack[:len(stack)-1]...)
			var width int
			if len(stack) > 0 {
				width = last - stack[len(stack)-1]
			} else {
				width = last + 1
			}
			if result < heights[h]*width {
				result = heights[h] * width
			}
		}
	}
	return result
}

func main() {
	// heights := []int{2, 1, 5, 6, 2, 3}
	heights := []int{2, 4}
	result := largestRectangleArea(heights)
	println("result:", result)
}
