package main

import "fmt"

func generateMatrix(n int) [][]int {
	if n == 1 {
		return [][]int{{1}}
	}
	result := make([][]int, n)
	for i := range result {
		result[i] = make([]int, n)
	}
	var value, x, y int
	up, down, left, right := 0, n-1, 0, n-1
	value++
	for up <= down && left <= right {
		// 从左到右
		for y = left; y <= right && left <= right && up <= down; y++ {
			result[x][y] = value
			value++
		}
		y--
		up++
		// 从上到下
		for x = up; x <= down && left <= right && up <= down; x++ {
			result[x][y] = value
			value++
		}
		x--
		right--
		// 从右到左
		for y = right; y >= left && left <= right && up <= down; y-- {
			result[x][y] = value
			value++
		}
		y++
		down--
		// 从下到上
		for x = down; x >= up && left <= right && up <= down; x-- {
			result[x][y] = value
			value++
		}
		x++
		left++
	}
	return result
}

func main() {
	n := 3
	fmt.Println(n / 2)
	result := generateMatrix(n)
	for _, r := range result {
		fmt.Println(r)
	}
}
