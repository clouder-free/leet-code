package main

import "fmt"

// dp
func minCut(s string) int {
	// 1.length of s
	if len(s) < 2 {
		return 0
	}
	// 2.dp init
	dp := make([]int, len(s))
	for i := 0; i < len(s); i++ {
		dp[i] = i
	}
	fmt.Printf("dp init:%v\n", dp)
	// 3.traverse
	for i := 1; i < len(s); i++ {
		// s[:i] is palindrome string, no need to cut
		if checkPalindrome(s, 0, i) {
			dp[i] = 0
		} else {
			for j := 0; j < i; j++ {
				if checkPalindrome(s, j+1, i) {
					if dp[j]+1 < dp[i] {
						dp[i] = dp[j] + 1
					}
				}
			}
		}
	}
	fmt.Printf("dp result:%v\n", dp)
	return dp[len(dp)-1]
}

func checkPalindrome(s string, start, end int) bool {
	for i, j := start, end; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}

func main() {
	s := "aab"
	result := minCut(s)
	fmt.Printf("result:%v\n", result)
}
