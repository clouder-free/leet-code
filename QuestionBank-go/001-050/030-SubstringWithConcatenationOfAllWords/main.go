package main

import "fmt"

/*
串联所有单词的子串
*/

func findSubstring(s string, words []string) []int {
	wordLen := len(words[0])
	wordMap := map[string]int{}
	for _, word := range words {
		wordMap[word] += 1
	}

	result := []int{}
	for i := 0; i < wordLen; i += 1 {
		fmt.Println("i:", i)
		left, right := i, i
		for right <= len(s)-wordLen {
			word := string(s[right : right+wordLen])
			fmt.Printf("1 left:%d right:%d word:%s wordMap:%v\n", left, right, word, wordMap)
			if _, ok := wordMap[word]; ok {
				right += wordLen
				wordMap[word] -= 1
				for wordMap[word] < 0 {
					leftWord := string(s[left : left+wordLen])
					wordMap[leftWord] += 1
					left += wordLen
				}
				// 判断wordMap是否全为0
				flag := true
				for _, v := range wordMap {
					if v != 0 {
						flag = false
						break
					}
				}
				if flag {
					result = append(result, left)
					// 移动左指针
					leftWord := string(s[left : left+wordLen])
					wordMap[leftWord] += 1
					left += wordLen
				}
			} else {
				// 移动左指针 缩小窗口
				for left < right {
					leftWord := string(s[left : left+wordLen])
					wordMap[leftWord] += 1
					left += wordLen
				}
				// 跳过不存在的单词
				right += wordLen
				left = right
			}
			fmt.Printf("2 after left:%d right:%d wordMap:%v\n", left, right, wordMap)
			fmt.Println("-------------------------------")
		}
		// 恢复wordMap
		for left < right {
			leftWord := string(s[left : left+wordLen])
			wordMap[leftWord] += 1
			left += wordLen
		}
		fmt.Println("~~~~~~~~~~~~~~~~~~")
	}

	return result
}

func main() {
	// s := "barfoothefoobarman"
	// words := []string{"bar", "foo", "the"}
	// s := "wordgoodgoodgoodbestword"
	// words := []string{"word", "good", "best", "word"}
	// s := "barfoofoobarthefoobarman"
	// words := []string{"foo", "bar"}
	// s := "lingmindraboofooowingdingbarrwingmonkeypoundcake"
	// words := []string{"fooo", "barr", "wing", "ding", "wing"}
	s := "ababababab"
	words := []string{"ababa", "babab"}
	result := findSubstring(s, words)
	fmt.Println("result:", result)
}
