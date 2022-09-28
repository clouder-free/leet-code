package main

import "fmt"

// bfs
func solve(board [][]byte) {
	if len(board) == 0 || len(board[0]) == 0 {
		return
	}
	// 边界O修改为M
	// 首行
	for i := 0; i < len(board[0]); i++ {
		if board[0][i] == 'O' {
			bfs(0, i, board, 1)
		}
	}
	// 末行
	for i := 0; i < len(board[len(board)-1]); i++ {
		if board[len(board)-1][i] == 'O' {
			bfs(len(board)-1, i, board, 1)
		}
	}
	// 首列
	for i := 0; i < len(board); i++ {
		if board[i][0] == 'O' {
			bfs(i, 0, board, 1)
		}
	}
	// 末列
	for i := 0; i < len(board); i++ {
		if board[i][len(board[i])-1] == 'O' {
			bfs(i, len(board[i])-1, board, 1)
		}
	}

	// 中间区域
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			bfs(i, j, board, 0)
		}
	}

	// 将边界上的M修改为O
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if board[i][j] == 'M' {
				board[i][j] = 'O'
			}
		}
	}
}

func bfs(x, y int, board [][]byte, t int) {
	// t==1 边缘填充 t==0中央填充
	if board[x][y] != 'O' {
		return
	}
	if t == 0 {
		board[x][y] = 'X'
	} else if t == 1 {
		board[x][y] = 'M'
	}
	r := []int{-1, 0, 1, 0}
	c := []int{0, 1, 0, -1}
	for i := 0; i < len(r); i++ {
		if x+r[i] >= 0 && x+r[i] < len(board) && y+c[i] >= 0 && y+c[i] < len(board[0]) {
			bfs(x+r[i], y+c[i], board, t)
		}
	}
}

func main() {
	board := [][]byte{
		{'X', 'X', 'X', 'X'},
		{'X', 'O', 'O', 'X'},
		{'X', 'X', 'O', 'X'},
		{'X', 'O', 'X', 'X'},
	}
	solve(board)
	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", board[i])
	}

}
