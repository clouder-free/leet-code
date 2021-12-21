package main

import "fmt"

/*
电话号码的字母组合
*/

func letterCombinations(digits string) []string {
	letterMap := map[string]string{"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
	result := []string{}
	if digits == "" {
		return result
	}
	letters := letterMap[string(digits[0])]
	// fmt.Println("letters:", letters)
	for _, letter := range letters {
		if digits[1:] != "" {
			leftCombins := letterCombinations(digits[1:])
			for _, combin := range leftCombins {
				result = append(result, string(letter)+combin)
			}
		} else {
			result = append(result, string(letter))
		}
	}
	// fmt.Printf("%v\n", letters)
	return result
}

func main() {
	digits := "23"
	result := letterCombinations(digits)
	fmt.Printf("%v\n", result)

}
