package main
<<<<<<< HEAD

import "fmt"

var result [][]string

func partition(s string) [][]string {
	result = [][]string{}
	backtrace(s, 0, []string{})
	return result
}

func backtrace(s string, index int, t []string) {
	if index == len(s) {
		temp := make([]string, len(t))
		copy(temp, t)
		result = append(result, temp)
		return
	}
	fmt.Printf("s:%s index:%d t:%v\n", s, index, t)
	for i := index + 1; i <= len(s); i++ {
		if check(s[index:i]) {
			t = append(t, s[index:i])
			// 向下递归
			backtrace(s, i, t)
			// 回溯
			t = t[:len(t)-1]
		}
	}
}

func check(s string) bool {
	for i, j := 0, len(s)-1; i <= j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}

func main() {
	s := "aab"
	res := partition(s)
	for i := 0; i < len(res); i++ {
		fmt.Printf("%v\n", res)
	}
}
=======
>>>>>>> c129b40f8a89045388d5627db9e3bb990463b2e7
