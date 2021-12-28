package main

import "strings"

/*
实现strStr()函数
*/

func strStr(haystack string, needle string) int {
	if haystack == "" || needle == "" {
		return 0
	}
	return strings.Index(haystack, needle)
}

func main() {
	haystack := ""
	needle := ""
	result := strStr(haystack, needle)
	println("result:", result)
}
