package main

func twoSum(numbers []int, target int) []int {
	// double point
	for i, j := 0, len(numbers)-1; i < j; {
		if numbers[i]+numbers[j] == target {
			return []int{i + 1, j + 1}
		} else if numbers[i]+numbers[j] < target {
			i += 1
		} else {
			j -= 1
		}
	}
	return []int{-1, -1}
}

func main() {

}
