package main

import "fmt"

func minWindow(s string, t string) string {
	var result string
	if len(s) == 0 || len(t) == 0 {
		return result
	}
	left, right := 0, -1
	tm := make(map[uint8]int)
	var count int
	// 初始化
	for i := range t {
		tm[t[i]] += 1
	}
	for left < len(s) {
		if right+1 < len(s) && count < len(t) {
			right += 1
			if v, ok := tm[s[right]]; ok {
				if v > 0 {
					count += 1
				}
				tm[s[right]] = v - 1
			}
		} else {
			if v, ok := tm[s[left]]; ok {
				if tm[s[left]] == 0 {
					count -= 1
				}
				tm[s[left]] = v + 1
			}
			left += 1
		}
		if count == len(t) {
			if len(result) == 0 || len(result) > right-left+1 {
				result = s[left : right+1]
			}
		}
	}
	return result
}

func main() {
	s := "ADOBECODEBANC"
	t := "ABC"
	result := minWindow(s, t)
	fmt.Println("result:", result)
}
