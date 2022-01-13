package main

import (
	"fmt"
	"sort"
)

/*
组合总和II
*/

func combinationSum2(candidates []int, target int) [][]int {
	// 数组排序
	sort.Ints(candidates)
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
		if i > 0 && candidates[i] == candidates[i-1] {
			continue
		}
		if target-c >= 0 {
			result = combination(candidates[i+1:], append(cands, c), target-c, result)
		}
	}
	return result
}

func main() {
	candidates := []int{10, 1, 2, 7, 6, 1, 5}
	target := 8
	result := combinationSum2(candidates, target)
	for _, r := range result {
		fmt.Printf("%v\n", r)
	}
}
