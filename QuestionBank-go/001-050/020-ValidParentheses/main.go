package main

import "fmt"

/*
有效的括号
*/

func isValid(s string) bool {
	matchMap := map[string]string{"(": ")", "[": "]", "{": "}"}
	stack := []string{}
	for _, c := range s {
		if _, ok := matchMap[string(c)]; ok {
			stack = append(stack, string(c))
		} else {
			if len(stack) > 0 && string(c) == matchMap[stack[len(stack)-1]] {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		}
	}
	return len(stack) == 0
}

func main() {
	s := "{[]}"
	result := isValid(s)
	fmt.Println("s:", s, "result:", result)
}
