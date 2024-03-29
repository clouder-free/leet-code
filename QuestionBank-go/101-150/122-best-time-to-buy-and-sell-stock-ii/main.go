package main

import "fmt"

func maxProfit(prices []int) int {
	var profit int
	for i:=1;i<len(prices);i++{
		if prices[i] > prices[i-1] {
			profit += prices[i] - prices[i-1]
		}
	}
	return profit
}

func main() {
	prices := []int{7, 1, 5, 3, 6, 4}
	result := maxProfit(prices)
	fmt.Printf("result:%v\n", result)
}