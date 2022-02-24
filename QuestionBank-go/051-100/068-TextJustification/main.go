package main

import (
	"fmt"
	"strings"
)

func fullJustify(words []string, maxWidth int) []string {
	var result []string
	var temp []string
	// 添加首元素
	temp = append(temp, words[0])
	for i := 1; i < len(words); i++ {
		//fmt.Println("temp:", temp, "i:", i)
		if len(strings.Join(temp, " ")+" "+words[i]) > maxWidth {
			var s string
			totalSpace := maxWidth - len(strings.Join(temp, ""))
			if len(temp) == 1 {
				s += temp[0] + strings.Repeat(" ", totalSpace)
			} else {
				var avgSpace, leftSpace int
				// 空格平均分配到n-1个单词 n个单词 n-1个间隔
				avgSpace = totalSpace / (len(temp) - 1)
				// 剩余空格数
				leftSpace = totalSpace % (len(temp) - 1)
				// 开始遍历
				for j := 0; j < len(temp)-1; j++ {
					s += temp[j] + strings.Repeat(" ", avgSpace)
					// 左侧空格数要多余右侧 额外加一个空格 来保证相对均匀
					if j < leftSpace {
						s += " "
					}
				}
				s += temp[len(temp)-1]
			}
			result = append(result, s)
			// 清空temp
			temp = []string{}
		}
		// 直接添加到temp
		temp = append(temp, words[i])
		//fmt.Println("after temp:", temp, "i:", i)
	}
	// 判断temp不为空
	if len(temp) > 0 {
		ts := strings.Join(temp, " ")
		result = append(result, ts+strings.Repeat(" ", maxWidth-len(ts)))
	}
	return result
}

func main() {
	//words := []string{"This", "is", "an", "example", "of", "text", "justification."}
	words := []string{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}
	maxWidth := 20
	result := fullJustify(words, maxWidth)
	fmt.Printf("%v\n", result)
	for _, r := range result {
		fmt.Printf("%s\n", r)
	}
}
