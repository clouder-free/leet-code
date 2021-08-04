package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	var result int
	var dict = make(map[string]int)
	for i, j := 0, 0; j < len(s); j++ {
		fmt.Printf("dict: %v\n", dict)
		fmt.Printf("i: %d j: %d\n", i, j)
		index, ok := dict[string(s[j])]
		if ok && index >= i {
			i = index + 1
		}
		dict[string(s[j])] = j
		if result < j-i+1 {
			result = j - i + 1
		}
		println("result:", result)
	}
	return result
}

func main() {
	// s := "pwwkew"
	// s := "abcabcabc"
	// s := "bbbbb"
	s := "abba"
	result := lengthOfLongestSubstring(s)
	fmt.Println("result:", result)

}
