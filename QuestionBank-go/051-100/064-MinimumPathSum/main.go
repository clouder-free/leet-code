package main

import "fmt"

func minPathSum(grid [][]int) int {
	// 行 列
	m, n := len(grid), len(grid[0])
	// 初始化 行 列
	for i := 1; i < n; i++ {
		grid[0][i] += grid[0][i-1]
	}
	for i := 1; i < m; i++ {
		grid[i][0] += grid[i-1][0]
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if grid[i-1][j] < grid[i][j-1] {
				grid[i][j] += grid[i-1][j]
			} else {
				grid[i][j] += grid[i][j-1]
			}
		}
	}
	return grid[m-1][n-1]
}

func main() {
	grid := [][]int{
		{1, 3, 1}, {1, 5, 1}, {4, 2, 1},
	}
	result := minPathSum(grid)
	fmt.Println("result:", result)
}
