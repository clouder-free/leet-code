package main

func mySqrtx(x int) int {
	if x == 0 {
		return x
	}
	left, right := 1, x/2
	for left < right {
		mid := (left + right + 1) / 2
		if mid*mid == x {
			return mid
		} else if mid*mid > x {
			right = mid - 1
		} else {
			left = mid
		}
	}
	return left

}

func main() {

}
