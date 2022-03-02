package main

import "fmt"

var result [][]int

func combine(n int, k int) [][]int {
	// 初始化
	result = [][]int{}
	numbers := make([]int, n)
	for i := 0; i < n; i++ {
		numbers[i] = i + 1
	}
	if n == k {
		result = append(result, numbers)
		return result
	}
	backtrace(numbers, []int{}, k)
	return result
}

func backtrace(numbers []int, temp []int, k int) {
	//fmt.Println("backtrace numbers:", numbers, "temp:", temp, "k:", k, "result:", result)
	if len(temp) == k {
		t := make([]int, k)
		copy(t, temp)
		result = append(result, t)
		return
	}
	for i := range numbers {
		var nums []int
		nums = append(nums, numbers[i+1:]...)
		temp = append(temp, numbers[i])
		backtrace(nums, temp, k)
		// 回溯 恢复原状态
		temp = temp[:len(temp)-1]
	}
}

func main() {
	n, k := 4, 2
	res := combine(n, k)
	for i := range res {
		fmt.Println(res[i])
	}
}
