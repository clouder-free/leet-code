package main

import (
	"fmt"
	"strings"
)

func lengthOfLastWorld(s string) int {
	// 去除左右的空格
	s = strings.TrimSpace(s)
	// 按空格分割
	sli := strings.Split(s, " ")
	// 返回最后一个单词的长度
	return len(sli[len(sli)-1])
}

func main() {
	//s := "Hello World"
	//s := "   fly me   to  the moon  "
	s := "luffy is still joyboy"
	result := lengthOfLastWorld(s)
	fmt.Printf("%v\n", result)
}
