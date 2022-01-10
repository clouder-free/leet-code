package main

import "fmt"

/*
有效的数独
*/

func isValidSudoku(board [][]byte) bool {
	// 行数 列数
	r, c := len(board), len(board[0])
	// 行
	for i := 0; i < r; i += 1 {
		rows := map[string]bool{}
		for j := 0; j < c; j += 1 {
			r := string(board[i][j])
			if r != "." {
				// 不存在该元素
				if !rows[r] {
					rows[r] = true
					continue
				}
				return false
			}
		}
	}
	// 列
	for i := 0; i < c; i += 1 {
		cols := map[string]bool{}
		for j := 0; j < r; j += 1 {
			c := string(board[j][i])
			if c != "." {
				if !cols[c] {
					cols[c] = true
					continue
				}
				return false
			}
		}
	}
	// 九宫格
	for i := 0; i < r; i += 3 {
		for j := 0; j < c; j += 3 {
			// 九宫格元素
			grids := map[string]bool{}
			for m := i; m < i+3; m += 1 {
				for n := j; n < j+3; n += 1 {
					g := string(board[m][n])
					if g != "." {
						if grids[g] {
							return false
						} else {
							grids[g] = true
						}
					}
				}
			}
		}
	}

	return true
}

func main() {
	board := [][]byte{
		{byte('8'), byte('3'), byte('.'), byte('.'), byte('7'), byte('.'), byte('.'), byte('.'), byte('.')},
		{byte('6'), byte('.'), byte('.'), byte('1'), byte('9'), byte('5'), byte('.'), byte('.'), byte('.')},
		{byte('.'), byte('9'), byte('8'), byte('.'), byte('.'), byte('.'), byte('.'), byte('6'), byte('.')},
		{byte('8'), byte('.'), byte('.'), byte('.'), byte('6'), byte('.'), byte('.'), byte('.'), byte('3')},
		{byte('4'), byte('.'), byte('.'), byte('8'), byte('.'), byte('3'), byte('.'), byte('.'), byte('1')},
		{byte('7'), byte('.'), byte('.'), byte('.'), byte('2'), byte('.'), byte('.'), byte('.'), byte('6')},
		{byte('.'), byte('6'), byte('.'), byte('.'), byte('.'), byte('.'), byte('2'), byte('8'), byte('.')},
		{byte('.'), byte('.'), byte('.'), byte('4'), byte('1'), byte('9'), byte('.'), byte('.'), byte('5')},
		{byte('.'), byte('.'), byte('.'), byte('.'), byte('8'), byte('.'), byte('.'), byte('7'), byte('9')},
	}
	result := isValidSudoku(board)
	fmt.Println("result:", result)
}

/*
[[".",".","4",".",".",".","6","3","."],
 [".",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".","9","."],
 [".",".",".","5","6",".",".",".","."],
 ["4",".","3",".",".",".",".",".","1"],
 [".",".",".","7",".",".",".",".","."],
 [".",".",".","5",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]
*/
