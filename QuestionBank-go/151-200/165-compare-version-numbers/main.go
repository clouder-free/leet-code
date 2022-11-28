package main

import (
	"fmt"
	"strconv"
	"strings"
)

func compareVersion(version1 string, version2 string) int {
	v1 := strings.Split(version1, ".")
	v2 := strings.Split(version2, ".")
	for i := 0; i < len(v1) || i < len(v2); {
		var s1, s2 int
		if i < len(v1) {
			s1, _ = strconv.Atoi(v1[i])
		}
		if i < len(v2) {
			s2, _ = strconv.Atoi(v2[i])
		}
		if s1 > s2 {
			return 1
		} else if s1 < s2 {
			return -1
		} else {
			i += 1
		}
	}
	return 0
}

func main() {
	version1 := "1.0"
	version2 := "1.01.0"
	result := compareVersion(version1, version2)
	fmt.Printf("result:%v\n", result)
}
