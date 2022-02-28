package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
	// 确定行
	row := -1
	for i := 0; i < len(matrix); i++ {
		if matrix[i][len(matrix[i])-1] >= target {
			row = i
			break
		}
	}
	if row == -1 {
		return false
	}
	// 确定行 单行二分法
	left, right := 0, len(matrix[row])-1
	for left <= right {
		mid := (left + right) / 2
		if matrix[row][mid] == target {
			return true
		} else if matrix[row][mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return false
}

func main() {
	matrix := [][]int{
		{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 50},
	}
	target := 10
	result := searchMatrix(matrix, target)
	fmt.Println("result:", result)
}
