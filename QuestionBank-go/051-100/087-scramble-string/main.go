package main

import (
	"sort"
	"strings"
)

func isScramble(s1 string, s2 string) bool {
	// string length
	if len(s1) != len(s2) {
		return false
	}
	if s1 == s2 {
		return true
	}
	ss1 := strings.Split(s1, "")
	sort.Strings(ss1)
	ss2 := strings.Split(s2, "")
	sort.Strings(ss2)
	if strings.Join(ss1, "") != strings.Join(ss2, "") {
		return false
	}
	length := len(s1)
	for i := 1; i < length; i++ {
		l1, r1 := s1[:i], s1[i:]
		l2, r2 := s2[:i], s2[i:]
		if isScramble(l1, l2) && isScramble(r1, r2) {
			return true
		}
		l2, r2 = s2[:length-i], s2[length-i:]
		if isScramble(l1, r2) && isScramble(r1, l2) {
			return true
		}
	}
	return false
}

// during recursion, there are repeatable compution. then store the little compution.
func isScramble2(s1 string, s2 string) bool {
	// value: -1 返回false 0 不存在继续递归 1 返回true
	cache := make(map[string]int)
	return scramble(s1, s2, cache)
}

func scramble(s1 string, s2 string, cache map[string]int) bool {
	if len(s1) != len(s2) {
		return false
	}
	if s1 == s2 {
		return true
	}
	// get result from cache
	value := cache[strings.Join([]string{s1, s2}, "#")]
	if value == -1 {
		return false
	} else if value == 1 {
		return true
	}
	// sort s1 s2
	ss1 := strings.Split(s1, "")
	sort.Strings(ss1)
	ss2 := strings.Split(s2, "")
	sort.Strings(ss2)
	if strings.Join(ss1, "") != strings.Join(ss2, "") {
		// store cache
		cache[strings.Join([]string{s1, s2}, "#")] = -1
		return false
	}
	length := len(s1)
	for i := 1; i < length; i++ {
		// s1[:i] s1[i:]
		// s2[:i] s2[i:] / s2[:length-i] s2[length-i:]
		if (scramble(s1[:i], s2[:i], cache) && scramble(s1[i:], s2[i:], cache)) || (scramble(s1[:i], s2[length-i:], cache) && scramble(s1[i:], s2[:length-i], cache)) {
			// store cache
			cache[strings.Join([]string{s1, s2}, "#")] = 1
			return true
		}
	}
	cache[strings.Join([]string{s1, s2}, "#")] = -1
	return false
}

func main() {
	s1 := "abcde"
	s2 := "caebd"
	result := isScramble2(s1, s2)
	println("result:", result)
}
