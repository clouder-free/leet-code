package main

import "strings"

/*
最长公共前缀
*/

func longestCommonPrefix(strs []string) string {
	if strs == nil || len(strs) == 0 {
		return ""
	}
	var result string
	for i := 1; ; i++ {
		prefix := ""
		if i > len(strs[0]) || strs[0][:i] == "" {
			return result
		}
		prefix = strs[0][:i]
		for _, str := range strs[1:] {
			if i > len(str) || !strings.HasPrefix(str, prefix) {
				return result
			}
		}
		result = prefix
	}
}

func main() {
	// strs := []string{"flower", "flow", "flight"}
	// strs := []string{"dog", "racecar", "car"}
	// strs := []string{"a"}
	strs := []string{""}
	result := longestCommonPrefix(strs)
	println(result)
}
