package main

/*
罗马数字转整数

*/
func romanToInt(s string) int {
	rti := map[string]int{
		"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90,
		"C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000,
	}
	var result int
	for s != "" {
		if len(s) >= 2 && (string(s[0]) == "I" || string(s[0]) == "X" || string(s[0]) == "C") {
			if v, ok := rti[string(s[:2])]; ok {
				result += v
				s = string(s[2:])
				continue
			}
		}
		v, _ := rti[string(s[0])]
		result += v
		s = string(s[1:])
	}
	return result
}

func main() {
	// s := "III"
	s := "MCMXCIV"
	result := romanToInt(s)
	println("result:", result)
}
