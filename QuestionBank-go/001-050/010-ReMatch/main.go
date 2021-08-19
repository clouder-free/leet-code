package main

/*
正则表达式匹配
*/

func isMatch(s string, p string) bool {
	// 以p为准来进行判断
	if p == "" {
		return s == ""
	}
	if len(p) == 1 {
		return len(s) == 1 && (s == p || p == ".")
	}
	if len(p) >= 2 && string(p[1]) == "*" {
		// 首字符匹配
		if len(s) > 0 && (string(s[0]) == string(p[0]) || string(p[0]) == ".") {
			return isMatch(s[1:], p) || isMatch(s, p[2:])
		} else {
			return isMatch(s, p[2:])
		}
	} else {
		if len(s) > 0 && (string(s[0]) == string(p[0]) || string(p[0]) == ".") {
			return isMatch(s[1:], p[1:])
		} else {
			return false
		}
	}
}

func main() {
	s := "aab"
	p := "c*a*b"
	result := isMatch(s, p)
	println("result:", result)
}
