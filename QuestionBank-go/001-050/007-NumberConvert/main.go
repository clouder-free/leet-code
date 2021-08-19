package main

import (
	"math"
	"strconv"
	"strings"
)

/*
数字反转
*/

func reverse(x int) int {
	if x == 0 {
		return x
	}
	res := ""
	s := strconv.Itoa(x)
	if string(s[0]) == "-" {
		res += "-"
	}
	// 去除左侧的- 右侧的0
	s = strings.TrimRight(strings.TrimLeft(s, "-"), "0")
	for i := len(s) - 1; i > -1; i-- {
		res += string(s[i])
	}
	r, _ := strconv.Atoi(res)
	if r > int(math.Pow(2, 31)-1) || r < int(math.Pow(-2, 31)) {
		return 0
	}
	return r
}

func main() {
	x := 123
	println(x)
	result := reverse(x)
	println(result)
}
