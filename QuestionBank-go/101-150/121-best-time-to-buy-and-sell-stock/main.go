package main

import "fmt"

func maxProfit(prices []int) int {
	var result int
	minPrice := prices[0]
	for i := 0; i < len(prices); i++ {
		if minPrice > prices[i] {
			minPrice = prices[i]
		}
		if result < prices[i]-minPrice {
			result = prices[i] - minPrice
		}
	}
	return result
}

func main() {
	// prices := []int{7, 1, 5, 3, 6, 4}
	prices := []int{7, 6, 4, 3, 1}
	result := maxProfit(prices)
	fmt.Printf("result:%v\n", result)

}
