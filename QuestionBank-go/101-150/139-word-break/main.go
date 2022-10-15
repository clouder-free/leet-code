package main

import "fmt"

func wordBreak(s string, wordDict []string) bool {
	// double pointer
	dp := make([]bool, len(s)+1)
	dp[0] = true
	for i := 1; i <= len(s); i++ {
		for _, word := range wordDict {
			if i >= len(word) && dp[i-len(word)] && word == s[i-len(word):i] {
				dp[i] = true
				break
			}
		}
	}
	return dp[len(dp)-1]

}

func main() {
	s := "aaaaaaa"
	wordDict := []string{"aaa", "aaaa"}
	result := wordBreak(s, wordDict)
	fmt.Printf("result:%v\n", result)

}
