package main

import "fmt"

func getRow(rowIndex int) []int {
	if rowIndex == 0 {
		return []int{1}
	}
	if rowIndex == 1 {
		return []int{1, 1}
	}
	result := []int{1, 1}
	for i := 1; i < rowIndex; i++ {
		res := []int{1}
		for j := 1; j < len(result); j++ {
			res = append(res, result[j]+result[j-1])
		}
		res = append(res, 1)
		result = res[:]
	}
	return result
}

func main() {
	rowIndex := 4
	result := getRow(rowIndex)
	fmt.Printf("%v\n", result)
}
