package main

import "fmt"

/*
最长有效括号
*/

func longestValidParentheses(s string) int {
	if s == "" {
		return 0
	}
	result, start := 0, 0
	stack := []int{}
	for i := 0; i < len(s); i += 1 {
		if string(s[i]) == "(" {
			stack = append(stack, i)
		} else if len(stack) > 0 {
			stack = stack[:len(stack)-1]
			if len(stack) > 0 {
				if i-stack[len(stack)-1] > result {
					result = i - stack[len(stack)-1]
				}
			} else {
				if i-start+1 > result {
					result = i - start + 1
				}
			}
		} else {
			start = i + 1
		}
	}
	return result
}

func main() {
	s := "(()"
	result := longestValidParentheses(s)
	fmt.Println("result:", result)
}
