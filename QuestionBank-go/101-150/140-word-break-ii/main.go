package main

import "fmt"

func wordBreak(s string, wordDict []string) []string {
	memo := make(map[string][]string)
	return dfs(s, wordDict, memo)
}

func dfs(s string, wordDict []string, memo map[string][]string) []string {
	if len(memo[s]) > 0 {
		return memo[s]
	}

	if s == "" {
		return nil
	}

	result := []string{}
	for _, word := range wordDict {
		if len(s) >= len(word) {
			fmt.Printf("s:%v word:%v\n", s, word)
			if s[:len(word)] != word {
				continue
			}
			if len(s) == len(word) {
				result = append(result, word)
				continue
			}
			for _, r := range dfs(s[len(word):], wordDict, memo) {
				result = append(result, word+" "+r)
			}
		}
	}
	memo[s] = result
	return result
}

func main() {
	s := "pineapplepenapple"
	wordDict := []string{"apple", "pen", "applepen", "pine", "pineapple"}
	result := wordBreak(s, wordDict)
	fmt.Printf("result length:%v\n", len(result))
	for _, r := range result {
		fmt.Printf("%v\n", r)
	}
}
