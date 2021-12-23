package main

import (
	"fmt"
	"strings"
)

/*
括号生成
*/

func generateParenthesis(n int) []string {
	result := []string{}
	return generate(n, "", result)
}

func generate(n int, s string, result []string) []string {
	if len(s) == n*2 {
		result = append(result, s)
		return result
	}
	if strings.Count(s, "(") < n {
		result = generate(n, s+"(", result)
	}
	if strings.Count(s, "(") > strings.Count(s, ")") {
		result = generate(n, s+")", result)
	}
	return result
}

func main() {
	n := 3
	result := generateParenthesis(n)
	fmt.Printf("%v\n", result)
}
