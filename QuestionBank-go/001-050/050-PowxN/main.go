package main

import "fmt"

func myPow(x float64, n int) float64 {
	if n == 0 {
		return 1.0
	} else if n < 0 {
		return 1 / myPow(x, -n)
	} else if n%2 == 1 {
		return myPow(x*x, n/2) * x
	} else {
		return myPow(x*x, n/2)
	}
}

func main() {
	result := myPow(2.0, 10)
	fmt.Printf("%v\n", result)
}
