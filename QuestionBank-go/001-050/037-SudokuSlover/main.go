package main

import (
	"fmt"
)

/*
解数独
*/

func solveSudoku(board [][]byte) {
	// 数据初始化 行/列/宫格
	m, n := len(board), len(board[0])
	rows, cols, cubes := []map[int]bool{}, []map[int]bool{}, []map[int]bool{}
	dots := [][]int{}

	for i := 1; i < 10; i += 1 {
		rows = append(rows, map[int]bool{1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true, 8: true, 9: true})
		cols = append(cols, map[int]bool{1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true, 8: true, 9: true})
		cubes = append(cubes, map[int]bool{1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true, 8: true, 9: true})
	}
	// 初始数据
	for i := 0; i < m; i += 1 {
		for j := 0; j < n; j += 1 {
			b := board[i][j]
			if string(b) == "." {
				dots = append(dots, []int{i, j})
			} else {
				delete(rows[i], int(b))
				delete(cols[j], int(b))
				delete(cubes[i/3*3+j/3], int(b))
			}
		}
	}
	_, board = backtrace(board, dots, rows, cols, cubes)
	for i, b := range board {
		fmt.Printf("board[%d]:%v\n", i, b)
	}
}

func backtrace(board [][]byte, dots [][]int, rows []map[int]bool, cols []map[int]bool, cubes []map[int]bool) (bool, [][]byte) {
	if len(dots) <= 0 {
		return true, board
	}
	i, j := dots[0][0], dots[0][1]
	values := []int{}
	for k := 1; k < 10; k += 1 {
		if rows[i][k] && cols[j][k] && cubes[i/3*3+j/3][k] {
			values = append(values, k)
		}
	}
	for _, val := range values {
		delete(rows[i], val)
		delete(cols[j], val)
		delete(cubes[i/3*3+j/3], val)
		board[i][j] = byte(val)
		if ok, board := backtrace(board, dots[1:], rows, cols, cubes); ok {
			return true, board
		}
		// 回溯
		rows[i][val] = true
		cols[j][val] = true
		cubes[i/3*3+j/3][val] = true
	}
	return false, board
}

func main() {
	board := [][]byte{
		{byte('5'), byte('3'), byte('.'), byte('.'), byte('7'), byte('.'), byte('.'), byte('.'), byte('.')},
		{byte('6'), byte('.'), byte('.'), byte('1'), byte('9'), byte('5'), byte('.'), byte('.'), byte('.')},
		{byte('.'), byte('9'), byte('8'), byte('.'), byte('.'), byte('.'), byte('.'), byte('6'), byte('.')},
		{byte('8'), byte('.'), byte('.'), byte('.'), byte('6'), byte('.'), byte('.'), byte('.'), byte('3')},
		{byte('4'), byte('.'), byte('.'), byte('8'), byte('.'), byte('3'), byte('.'), byte('.'), byte('1')},
		{byte('7'), byte('.'), byte('.'), byte('.'), byte('2'), byte('.'), byte('.'), byte('.'), byte('6')},
		{byte('.'), byte('6'), byte('.'), byte('.'), byte('.'), byte('.'), byte('2'), byte('8'), byte('.')},
		{byte('.'), byte('.'), byte('.'), byte('4'), byte('1'), byte('9'), byte('.'), byte('.'), byte('5')},
		{byte('.'), byte('.'), byte('.'), byte('.'), byte('8'), byte('.'), byte('.'), byte('7'), byte('9')},
	}
	solveSudoku(board)
}
