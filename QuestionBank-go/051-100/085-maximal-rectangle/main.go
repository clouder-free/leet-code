package main

// 084-largest-rectangle-in-histogram
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

func maximalRectangle(matrix [][]byte) int {
	var result int
	matrixRectangle := make([][]int, len(matrix))
	for i := 0; i < len(matrix); i++ {
		matrixRectangle[i] = make([]int, len(matrix[i]))
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == '1' {
				if i == 0 {
					matrixRectangle[i][j] = 1
				} else {
					matrixRectangle[i][j] = matrixRectangle[i-1][j] + 1
				}
			}
		}
	}
	for i := 0; i < len(matrixRectangle); i++ {
		area := largestRectangleArea(matrixRectangle[i])
		if result < area {
			result = area
		}
	}
	return result
}

func main() {
	matrix := [][]byte{
		{'1', '0', '1', '0', '0'},
		{'1', '0', '1', '1', '1'},
		{'1', '1', '1', '1', '1'},
		{'1', '0', '0', '1', '0'},
	}
	result := maximalRectangle(matrix)
	println("result:", result)
}
