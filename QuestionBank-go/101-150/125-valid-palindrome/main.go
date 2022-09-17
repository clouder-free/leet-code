package main

import (
	"fmt"
	"strings"
	"unicode"
)

func isPalindrome(s string) bool {
	// to lower
	s = strings.ToLower(s)
	if s == "" {
		return true
	}
	// fmt.Printf("s:%v\n", s)
	for i, j := 0, len(s)-1; i <= j; {
		for ; i <= j && !unicode.IsNumber(rune(s[i])) && !unicode.IsLetter(rune(s[i])); i += 1 {
		}
		for ; i <= j && !unicode.IsNumber(rune(s[j])) && !unicode.IsLetter(rune(s[j])); j -= 1 {
		}
		if i <= j {
			if s[i] == s[j] {
				i += 1
				j -= 1
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	// s := "A man, a plan, a canal: Panama"
	s := "race a car"
	result := isPalindrome(s)
	fmt.Printf("result:%v\n", result)

}
