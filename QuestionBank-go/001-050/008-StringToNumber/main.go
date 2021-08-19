package main

import (
	"math"
	"strconv"
	"strings"
	"unicode"
)

func myAtoi(s string) int {
	// 左侧空格
	s = strings.TrimLeft(s, " ")
	if s == "" {
		return 0
	}
	res := ""
	// 读入字符
	for i := 0; i < len(s); i++ {
		if unicode.IsDigit(rune(s[i])) {
			res += string(s[i])
		} else if string(s[i]) == "-" && i == 0 {
			res += string(s[i])
		} else if string(s[i]) == "+" && i == 0 {
			continue
		} else {
			break
		}
	}
	if res == "" {
		return 0
	}
	r, _ := strconv.Atoi(res)
	if r < int(math.Pow(-2, 31)) {
		r = int(math.Pow(-2, 31))
	} else if r > int(math.Pow(2, 31))-1 {
		r = int(math.Pow(2, 31)) - 1
	}
	return r
}

func main() {
	// s := "    -42"
	// s := "4193 with words"
	// s := "words and 987"
	s := "-91283472332"
	res := myAtoi(s)
	println(res)
}
