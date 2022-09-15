package main

import "fmt"

func minimumTotal(triangle [][]int) int {
	for i := 1; i < len(triangle); i++ {
		for j := 0; j < len(triangle[i]); j++ {
			if j == 0 {
				triangle[i][j] += triangle[i-1][j]
			} else if j == len(triangle[i])-1 {
				triangle[i][j] += triangle[i-1][j-1]
			} else {
				if triangle[i-1][j-1] <= triangle[i-1][j] {
					triangle[i][j] += triangle[i-1][j-1]
				} else {
					triangle[i][j] += triangle[i-1][j]
				}
			}
		}
	}
	result := triangle[len(triangle)-1][0]
	for i := 0; i < len(triangle[len(triangle)-1]); i++ {
		if result > triangle[len(triangle)-1][i] {
			result = triangle[len(triangle)-1][i]
		}
	}
	// fmt.Printf("%v\n", triangle)
	return result
}

func main() {
	triangle := [][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}
	result := minimumTotal(triangle)
	fmt.Println("result:", result)
}
