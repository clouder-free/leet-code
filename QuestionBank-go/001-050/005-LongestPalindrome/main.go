package main

import (
	"strings"
)

/*
最长回文子串
*/

func longestPalindrome(s string) string {
	// 填充字符
	s = "#" + strings.Join(strings.Split(s, ""), "#") + "#"
	result := ""
	for index := range s {
		i, j := index, index
		for i >= 0 && j < len(s) {
			if s[i] == s[j] {
				i--
				j++
			} else {
				break
			}
		}
		r := strings.ReplaceAll(s[i+1:j], "#", "")
		if len(result) < len(r) {
			result = r
		}
	}
	return result
}

// 动态规划
func longestPalindrome2(s string) string {
	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
	}
	l, r := 0, 0
	for i := len(dp) - 1; i > 0; i-- {
		dp[i][i] = false
		for j := i + 1; j < len(dp); j++ {
			if s[i] == s[j] {
				if j-i < 3 {
					dp[i][j] = true
				} else {
					dp[i][j] = dp[i+1][j-1]
				}
			}
			if dp[i][j] && r-l < j-i {
				l, r = i, j
			}
		}
	}
	return s[l : r+1]
}

func main() {
	// s := "babad"
	s := "cbbd"
	// s := "a"
	// s := "ac"
	// println(s[2:4])
	result := longestPalindrome(s)
	println("result:", result)

}
