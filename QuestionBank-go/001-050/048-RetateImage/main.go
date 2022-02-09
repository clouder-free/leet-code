package main

import "fmt"

func rotate(matrix [][]int) {
	// 对角线互换
	for i := 0; i < len(matrix); i++ {
		for j := i + 1; j < len(matrix); j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
	// 行逆序
	for i := 0; i < len(matrix); i++ {
		for m, n := 0, len(matrix[i])-1; m < n; m, n = m+1, n-1 {
			matrix[i][m], matrix[i][n] = matrix[i][n], matrix[i][m]
		}
	}
	for i := range matrix {
		fmt.Printf("%v\n", matrix[i])
	}
}

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	for i := range matrix {
		fmt.Printf("%v\n", matrix[i])
	}
	rotate(matrix)

}
