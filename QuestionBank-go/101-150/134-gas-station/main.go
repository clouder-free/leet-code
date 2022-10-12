package main

import "fmt"

func canCompleteCircuit(gas []int, cost []int) int {
	current, total := 0, 0
	start := 0
	for i := 0; i < len(gas); i++ {
		current += gas[i] - cost[i]
		total += gas[i] - cost[i]
		if current < 0 {
			start = i + 1
			current = 0
		}
	}
	if total < 0 {
		return -1
	}
	return start
}

func main() {
	gas := []int{1, 2, 3, 4, 5}
	cost := []int{3, 4, 5, 1, 2}
	result := canCompleteCircuit(gas, cost)
	fmt.Printf("result:%v\n", result)
}
