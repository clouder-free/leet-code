package main

import (
	"fmt"
	"math"
)

func totalNQueens(n int) int {
	var result int
	queens := make([][]string, n)
	for i := range queens {
		queens[i] = make([]string, n)
		// 初始化
		for j := range queens[i] {
			queens[i][j] = "."
		}
	}
	backtrace(queens, 0, &result)
	return result
}

func backtrace(queens [][]string, n int, result *int) {
	if n == len(queens) {
		*result += 1
		return
	}
	// 第n行
	for i := range queens[n] {
		queens[n][i] = "Q"
		if valid(queens, n, i) {
			// 向下递归
			backtrace(queens, n+1, result)
		}
		// 回溯恢复
		queens[n][i] = "."
	}
}

func valid(queens [][]string, row, col int) bool {
	for i := 0; i < row; i++ {
		if queens[i][col] == "Q" {
			return false
		}
		var j int
		for ; j < len(queens[i]); j++ {
			if queens[i][j] == "Q" {
				break
			}
		}
		if math.Abs(float64(row-i)) == math.Abs(float64(col-j)) {
			return false
		}
	}
	return true
}
func main() {
	n := 8
	result := totalNQueens(n)
	fmt.Printf("n: %d result: %d\n", n, result)
}
