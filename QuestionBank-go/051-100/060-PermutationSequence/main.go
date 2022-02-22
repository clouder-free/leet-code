package main

import (
	"fmt"
	"strconv"
)

/**
n个数字有N!种排列
k%(n-1)!取哪个数字
剩余的数字再取余
*/
func getPermutation(n int, k int) string {
	// 生成列表
	numbers := make([]string, n)
	for i := 0; i < n; i++ {
		numbers[i] = strconv.Itoa(i + 1)
	}
	// 阶乘结果
	dp := make([]int, n+1)
	dp[0], dp[1] = 1, 1
	for i := 2; i <= n; i++ {
		dp[i] = i * dp[i-1]
	}
	k -= 1
	var result string
	for len(numbers) > 0 {
		// 整除取第几个组排列
		i := k / dp[len(numbers)-1]
		result += numbers[i]
		// 取余 赋值给k
		k = k % dp[len(numbers)-1]
		// 修改numbers
		var temp []string
		temp = append(append(temp, numbers[:i]...), numbers[i+1:]...)
		numbers = temp
	}
	return result
}

func main() {
	n, k := 4, 9
	result := getPermutation(n, k)
	fmt.Println("result:", result)
}
