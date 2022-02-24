package main

import "fmt"

// 递归
func climbStairs(n int) int {
	if n <= 2 {
		return n
	}
	return climbStairs(n-1) + climbStairs(n-2)
}

// 动态规划
func climbStairs2(n int) int {
	if n <= 2 {
		return n
	}
	dp := make([]int, n)
	// 初始化
	dp[0], dp[1] = 1, 2
	for i := 2; i < n; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	return dp[n-1]
}

func main() {
	result := climbStairs2(44)
	fmt.Println("result:", result)
}
