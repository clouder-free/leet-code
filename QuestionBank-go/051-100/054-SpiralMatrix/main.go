package main

import "fmt"

func spiralOrder(matrix [][]int) []int {
	var result []int
	if len(matrix) == 0 {
		return result
	}
	// 四周边界上下左右
	up, down, left, right := 0, len(matrix)-1, 0, len(matrix[0])-1
	var x, y int
	for up <= down && left <= right {
		// 从左到右
		for y = left; y <= right && left <= right && up <= down; y++ {
			result = append(result, matrix[x][y])
		}
		y--
		// 缩小上边界
		up++
		for x = up; x <= down && left <= right && up <= down; x++ {
			result = append(result, matrix[x][y])
		}
		x--
		// 缩小右边界
		right--
		for y = right; y >= left && left <= right && up <= down; y-- {
			result = append(result, matrix[x][y])
		}
		y++
		// 缩小下边界
		down--
		for x = down; x >= up && left <= right && up <= down; x-- {
			result = append(result, matrix[x][y])
		}
		x++
		// 缩小左边界
		left++
	}
	return result
}

func main() {
	matrix := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
	}
	result := spiralOrder(matrix)
	fmt.Printf("result: %v\n", result)
}
