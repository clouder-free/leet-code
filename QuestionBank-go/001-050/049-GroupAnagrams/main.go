package main

import (
	"fmt"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	strMap := make(map[string][]string)
	for i := range strs {
		var s []string
		for j := 0; j < len(strs[i]); j++ {
			s = append(s, string(strs[i][j]))
		}
		sort.Strings(s)
		ss := strings.Join(s, "")
		m := strMap[ss]
		m = append(m, strs[i])
		strMap[ss] = m
	}
	var result [][]string
	for _, value := range strMap {
		result = append(result, value)
	}
	return result
}

func main() {
	strs := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	result := groupAnagrams(strs)
	for i := range result {
		fmt.Printf("%v\n", result[i])
	}
}
