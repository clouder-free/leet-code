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

func main() {
	s1 := "great"
	s2 := "rgeat"
	result := isScramble(s1, s2)
	println("result:", result)
}
