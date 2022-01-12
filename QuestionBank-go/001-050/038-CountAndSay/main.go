package main

import "fmt"

/*
外观数组
*/

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	s := "1"
	for i := 2; i <= n; i += 1 {
		temp := ""
		j, count := 0, 0
		for ; j < len(s); j += 1 {
			if j == 0 {
				count += 1
				continue
			}
			if string(s[j-1]) == string(s[j]) {
				count += 1
			} else {
				temp += fmt.Sprintf("%d", count) + string(s[j-1])
				count = 1
			}
		}
		s = temp + fmt.Sprintf("%d", count) + string(s[j-1])
	}
	return s
}

func main() {
	for i := 1; i < 6; i += 1 {
		s := countAndSay(i)
		fmt.Printf("%d: %s\n", i, s)
	}
}
