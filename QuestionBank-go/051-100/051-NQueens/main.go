package main

import (
	"fmt"
	"math"
	"strings"
)

var result [][]string

func solveNQueens(n int) [][]string {
	var queens [][]string
	result = [][]string{}
	for i := 0; i < n; i++ {
		var q []string
		for j := 0; j < n; j++ {
			q = append(q, ".")
		}
		queens = append(queens, q)
	}
	backtrace(queens, 0)
	return result
}

func backtrace(queens [][]string, n int) {
	if n == len(queens) {
		// 停止向下递归
		var temp []string
		for i := range queens {
			temp = append(temp, strings.Join(queens[i], ""))
		}
		result = append(result, temp)
		return
	}
	for i := range queens[n] {
		queens[n][i] = "Q"
		// 判断是否有效 有效向下递归 否则回溯
		if valid(queens, n, i) {
			backtrace(queens, n+1)
		}
		queens[n][i] = "."
	}
}

func valid(queens [][]string, row, col int) bool {
	for i := 0; i < row; i++ {
		// 列
		if queens[i][col] == "Q" {
			return false
		}
		// 对角线
		var j int
		for ; j < len(queens[i]); j += 1 {
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
	result := solveNQueens(1)
	for _, res := range result {
		fmt.Printf("%v\n", res)
		fmt.Println("-----------------")
	}
	//for i := range result {
	//	fmt.Printf("%v\n", result[i])
	//}
}
