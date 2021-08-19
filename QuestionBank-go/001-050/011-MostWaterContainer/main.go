package main

/*
盛最多水的容器
*/

func maxArea(height []int) int {
	var result int
	for i, j := 0, len(height)-1; i < j; {
		width := j - i
		h := height[i]
		if height[i] > height[j] {
			h = height[j]
		}
		if result < width*h {
			result = width * h
		}
		if height[i] > height[j] {
			j--
		} else {
			i++
		}
	}
	return result
}

func main() {
	// height := []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	// height := []int{1, 1}
	// height := []int{4, 3, 2, 1, 4}
	// height := []int{1, 2, 1}
	height := []int{2, 3, 4, 5, 18, 17, 6}
	result := maxArea(height)
	println("result:", result)

}
