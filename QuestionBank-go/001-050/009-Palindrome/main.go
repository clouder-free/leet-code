package main

import "strconv"

func isPalindrome(x int) bool {
	s := strconv.Itoa(x)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if string(s[i]) != string(s[j]) {
			return false
		}
	}
	return true
}

func isPalindrome2(x int) bool {
	// 负数 末尾为0
	if (x < 0) || (x%10 == 0 && x != 0) {
		return false
	}
	invertx := 0
	for x > invertx {
		invertx = invertx*10 + x%10
		x = x / 10
	}
	return x == invertx || x == invertx/10
}

func main() {
	// x := 121
	x := 121
	println(x / 10)
	println(x % 10)
	result := isPalindrome2(x)
	println("result:", result)
}
