package main

import "fmt"

func isInterleave(s1 string, s2 string, s3 string) bool {
	if len(s1)+len(s2) != len(s3) {
		return false
	}
	l1, l2 := len(s1)+1, len(s2)+1
	dp := make([][]bool, l1)
	for i := 0; i < l1; i++ {
		dp[i] = make([]bool, l2)
	}
	dp[0][0] = true
	// init first row
	for i := 1; i < l2; i++ {
		dp[0][i] = dp[0][i-1] && s2[i-1] == s3[i-1]
	}
	// init first column
	for i := 1; i < l1; i++ {
		dp[i][0] = dp[i-1][0] && s1[i-1] == s3[i-1]
	}
	for i := 1; i < l1; i++ {
		for j := 1; j < l2; j++ {
			dp[i][j] = (dp[i][j-1] && s2[j-1] == s3[j-1+i]) || (dp[i-1][j] && s1[i-1] == s3[i-1+j])
		}
	}
	return dp[l1-1][l2-1]
}

func main() {
	s1 := "aabcc"
	s2 := "dbbca"
	s3 := "aadbbcbcac"
	result := isInterleave(s1, s2, s3)
	fmt.Println("result:", result)
}
