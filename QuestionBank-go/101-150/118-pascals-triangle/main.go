package main

import "fmt"

func generate(numRows int) [][]int {
	if numRows == 1 {
		return [][]int{{1}}
	}
	if numRows == 2 {
		return [][]int{{1}, {1, 1}}
	}
	result := [][]int{{1}, {1, 1}}
	for i := 2; i < numRows; i++ {
		res := []int{1}
		for j := 1; j < len(result[i-1]); j++ {
			res = append(res, result[i-1][j]+result[i-1][j-1])
		}
		res = append(res, 1)
		result = append(result, res[:])
	}
	return result
}

func main() {
	numRows := 4
	result := generate(numRows)
	for i := 0; i < len(result); i++ {
		fmt.Printf("%v\n", result[i])
	}
}
