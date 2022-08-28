package main

func numDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}
	s = "0" + s
	dp := []int{}
	for i:=0;i<len(s);i++{
		dp = append(dp, 1)
	}
	for i:=2;i<len(s);i++{
		if s[i] == '0' {
			if s[i-1] == '0' || s[i-1] > '2' {
				return 0
			} else {
				dp[i] = dp[i-2]
			}
		} else if s[i-1] == '0' {
			dp[i] = dp[i-1]
		} else {
			if "10" < s[i-1:i+1] && s[i-1:i+1] <= "26" {
				dp[i] = dp[i-1] + dp[i-2]
			} else {
				dp[i] = dp[i-1]
			}
		}
	}
	return dp[len(dp)-1]
}

func main() {
	s := "226"
	result := numDecodings(s)
	println(result)
}