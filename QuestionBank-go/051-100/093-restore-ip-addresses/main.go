package main

import (
	"fmt"
	"strconv"
	"strings"
)

var result []string

func restoreIpAddresses(s string) []string {
	// global variable init
	result = []string{}
	ipAddress(s, []string{})
	return result
}

func validIp(s string) bool {
	if s == "" || len(s) > 3 || (len(s) > 1 && s[0] == '0') {
		return false
	}
	i, _ := strconv.Atoi(s)
	return i >= 0 && i <= 255
}

func ipAddress(s string, res []string) {
	if len(res) == 4 {
		if s == "" {
			result = append(result, strings.Join(res, "."))
		}
		return
	}
	for i := 1; i < 4; i++ {
		if len(s) >= i && validIp(s[:i]) {
			ipAddress(s[i:], append(res, s[:i]))
		}
	}
}

func main() {
	s := "25525511135"
	result := restoreIpAddresses(s)
	fmt.Printf("35:%v\n", validIp("35"))
	fmt.Printf("%v\n", result)
}
