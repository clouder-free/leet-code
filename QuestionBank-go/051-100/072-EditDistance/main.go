package main

import "fmt"

func minDistance(word1 string, word2 string) int {
	// 判断非空
	if word1 == "" {
		return len(word2)
	}
	if word2 == "" {
		return len(word1)
	}
	// 动态规划 dp定义二维数组
	// dp[i][j]表示word1[i]到word2[j]的编辑距离
	// word1[i]==word2[j] 那么dp[i][j]=dp[i-1][j-1]
	// word1[i]!=word2[j] word1可以进行替换操作 或者删除操作 或者插入操作
	// 替换操作 意味着从dp[i-1][j-1]进行1次替换操作到达dp[i][j]
	// 删除操作 意味着从dp[i][j-1]进行1次删除操作到达dp[i][j]
	// 插入操作 意味着从dp[i-1][j]进行1次插入操作到达dp[i][j]
	// dp[i][j]=min(dp[i-1][j-1], dp[i][j-1])+1
	n1, n2 := len(word1), len(word2)
	dp := make([][]int, n2+1)
	for i := 0; i < n2+1; i++ {
		dp[i] = make([]int, n1+1)
	}
	// 初始化 首行 首列
	for i := 1; i < n1+1; i++ {
		dp[0][i] = dp[0][i-1] + 1
	}
	for i := 1; i < n2+1; i++ {
		dp[i][0] = dp[i-1][0] + 1
	}
	// 开始赋值
	for i := 1; i < n2+1; i++ {
		for j := 1; j < n1+1; j++ {
			if word1[j-1] == word2[i-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				// 替换 删除 插入
				dp[i][j] = min(min(dp[i-1][j-1], dp[i][j-1]), dp[i-1][j]) + 1
			}
		}
	}
	return dp[n2][n1]
}

func min(m int, n int) int {
	if m < n {
		return m
	} else {
		return n
	}
}

func main() {
	word1 := "a"
	word2 := "ab"
	result := minDistance(word1, word2)
	fmt.Println("result:", result)
}
