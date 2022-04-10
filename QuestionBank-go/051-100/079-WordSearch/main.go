package main

import "fmt"

// 回溯法
func backtrace(board [][]byte, visited [][]bool, i, j, k int, word string) bool {
	m, n := len(board), len(board[0])
	/* i, j 代表当前位置 k 代表word当前匹配位置*/
	if board[i][j] != word[k] {
		return false
	} else if k == len(word)-1 {
		return true
	}
	// 四个方向 上下左右
	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	visited[i][j] = true
	for _, d := range directions {
		nx, ny := i+d[0], j+d[1]
		if nx >= 0 && nx < m && ny >= 0 && ny < n {
			if !visited[nx][ny] {
				if backtrace(board, visited, nx, ny, k+1, word) {
					return true
				}
			}
		}
	}
	visited[i][j] = false
	return false
}

func exists(board [][]byte, word string) bool {
	m, n := len(board), len(board[0])
	visited := make([][]bool, m)
	for i:=0;i<m;i++{
		visited[i] = make([]bool, n)
	}
	// 遍历
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if backtrace(board, visited, i, j, 0, word) {
				return true
			}
		}
	}
	return false
}

func main() {
	board := [][]byte{
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	word := "ABCCED"
	result := exists(board, word)
	fmt.Println("result:", result)
}
