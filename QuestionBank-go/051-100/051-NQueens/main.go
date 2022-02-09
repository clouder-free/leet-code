package main

import "fmt"

func solveNQueens(n int) [][]string {

}

func main() {
	result := solveNQueens(4)
	for i := range result {
		fmt.Printf("%v\n", result[i])
	}
}
