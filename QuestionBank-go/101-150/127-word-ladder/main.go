package main

import "fmt"

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordMap := make(map[string]bool)
	for i := 0; i < len(wordList); i++ {
		wordMap[wordList[i]] = true
	}
	if !wordMap[endWord] {
		return 0
	}
	visited := make(map[string]bool)
	visited[beginWord] = true
	length := 1
	q := []string{beginWord}
	// bfs
	for len(q) > 0 {
		length += 1
		temp := []string{}
		nextToVisit := make(map[string]bool)
		for i := 0; i < len(q); i++ {
			for j := 0; j < len(q[i]); j++ {
				s := "abcdefghijklmnopqrstuvwxyz"
				for k := 0; k < len(s); k++ {
					word := q[i][:j] + string([]byte{s[k]}) + q[i][j+1:]
					if wordMap[word] {
						if !visited[word] {
							if word == endWord {
								return length
							}
							if !nextToVisit[word] {
								nextToVisit[word] = true
								temp = append(temp, word)
							}
						}
					}
				}
			}
		}
		for k := range nextToVisit {
			visited[k] = true
		}
		q = temp[:]
	}
	return 0
}

func main() {
	beginWord := "hit"
	endWord := "cog"
	wordList := []string{"hot", "dot", "dog", "lot", "log", "cog"}
	result := ladderLength(beginWord, endWord, wordList)
	fmt.Printf("result:%v\n", result)
}
