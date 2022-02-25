package main

import "fmt"

func setZeros(matrix [][]int) {
	m, n := len(matrix), len(matrix[0])
	// 记录一下应置0的行 列
	rows := make(map[int]bool)
	cols := make(map[int]bool)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == 0 {
				rows[i] = true
				cols[j] = true
			}
		}
	}
	// 将所处行列的元素置0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if rows[i] || cols[j] {
				matrix[i][j] = 0
			}
		}
	}
	for _, row := range matrix {
		fmt.Println(row)
	}
}

func main() {
	matrix := [][]int{
		{0, 0, 0, 5}, {4, 3, 1, 4}, {0, 1, 1, 4}, {1, 2, 1, 3}, {0, 0, 1, 1},
	}
	setZeros(matrix)
}
