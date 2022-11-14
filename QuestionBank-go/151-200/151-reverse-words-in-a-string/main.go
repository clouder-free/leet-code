package main

import (
	"fmt"
	"strings"
)

func reverseWords(s string) string {
	// trim space left and right
	words := strings.Split(strings.TrimSpace(s), " ")
	filterWords := []string{}
	for i := 0; i < len(words); i++ {
		if words[i] != "" {
			filterWords = append([]string{words[i]}, filterWords...)
		}
	}
	return strings.Join(filterWords, " ")
}

func main() {
	s := "  hello    world  "
	result := reverseWords(s)
	fmt.Printf("result:%s\n", result)
}
