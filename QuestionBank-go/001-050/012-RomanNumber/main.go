package main

/*
整数数字转罗马数字
I             1
IV            4
V             5
IX            9
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900
M             1000
*/
func intToRoman(num int) string {
	var result string
	for num > 0 {
		if num >= 1000 {
			result += "M"
			num -= 1000
		} else if num >= 500 {
			if num >= 900 {
				result += "CM"
				num -= 900
			} else {
				result += "D"
				num -= 500
			}
		} else if num >= 100 {
			if num >= 400 {
				result += "CD"
				num -= 400
			} else {
				result += "C"
				num -= 100
			}
		} else if num >= 50 {
			if num >= 90 {
				result += "XC"
				num -= 90
			} else {
				result += "L"
				num -= 50
			}
		} else if num >= 10 {
			if num >= 40 {
				result += "XL"
				num -= 40
			} else {
				result += "X"
				num -= 10
			}
		} else if num >= 5 {
			if num == 9 {
				result += "IX"
				num -= 9
			} else {
				result += "V"
				num -= 5
			}
		} else if num == 4 {
			result += "IV"
			num -= 4
		} else {
			result += "I"
			num -= 1
		}
	}
	return result
}

func main() {
	// num := 3
	// num := 4
	// num := 9
	// num := 58
	num := 1994
	result := intToRoman(num)
	println("result:", result)
}
