package main

import (
	"fmt"
	"sort"
)

/*
组合总和
*/

func combinationSum(candidates []int, target int) [][]int {
	// 原数组排序
	sort.Ints(candidates)
	fmt.Printf("sorted: %v\n", candidates)
	return combination(candidates, []int{}, target, [][]int{})
}

func combination(candidates []int, cands []int, target int, result [][]int) [][]int {
	if target == 0 {
		tmp := make([]int, len(cands))
		copy(tmp, cands)
		result = append(result, tmp)
		return result
	}
	for i, c := range candidates {
		if target-c >= 0 {
			result = combination(candidates[i:], append(cands, c), target-c, result)
		}
	}
	return result
}

func main() {
	candidates := []int{2, 7, 6, 3, 5, 1}
	target := 9
	result := combinationSum(candidates, target)
	for _, r := range result {
		fmt.Printf("%v\n", r)
	}
}
