package main

import "fmt"

func numDistinct(s string, t string) int {
	// dp
	ls, lt := len(s), len(t)
	dp := make([][]int, lt)
	for i := 0; i < lt; i++ {
		dp[i] = make([]int, ls)
	}
	for i := 0; i < lt; i++ {
		for j := 0; j < ls; j++ {
			if t[i] == s[j] {
				if i == 0 {
					dp[i][j] = 1
				} else {
					for k := 0; k < j; k++ {
						dp[i][j] += dp[i-1][k]
					}
				}
			}
		}
	}
	var result int
	for i := 0; i < ls; i++ {
		result += dp[lt-1][i]
	}
	for i := 0; i < lt; i++ {
		fmt.Printf("%v\n", dp[i])
	}

	return result
}

func main() {
	s := "rabbbit"
	t := "rabbit"
	result := numDistinct(s, t)
	fmt.Printf("result:%v\n", result)
}
