package main

func numTrees(n int) int {
	c := 1
	for i := 0; i < n; i++ {
		c = 2 * c * (2*i + 1) / (i + 2)
	}
	return c
}

func main() {
	result := numTrees(3)
	println("result:", result)
}
