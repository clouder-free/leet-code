package main

import (
	"fmt"
	"strings"
)

func isNumber(s string) bool {
	if s == "" || strings.Trim(s, " ") == "" {
		return false
	}
	var num, e, dot bool
	nume := true
	s = strings.Trim(s, " ")
	for i, c := range s {
		if c == ' ' {
			return false
		}
		if c == '+' || c == '-' {
			if i > 0 && s[i-1] != 'e' {
				return false
			}
		} else if c >= '0' && c <= '9' {
			num = true
			nume = true
		} else if c == '.' {
			if dot || e {
				return false
			}
			dot = true
		} else if c == 'e' || c == 'E' {
			if e || !num {
				return false
			}
			e = true
			nume = false
		} else {
			return false
		}
	}
	return num && nume
}

func main() {
	s := "0"
	result := isNumber(s)
	fmt.Println("result:", result)
}
