package main

type MinStack struct {
	Stack []int
	Mins  []int
}

func Constructor() MinStack {
	return MinStack{
		Stack: []int{},
		Mins:  []int{},
	}
}

func (this *MinStack) Push(val int) {
	if len(this.Stack) == 0 || this.Mins[len(this.Mins)-1] >= val {
		this.Mins = append(this.Mins, val)
	}
	this.Stack = append(this.Stack, val)
}

func (this *MinStack) Pop() {
	if this.Stack[len(this.Stack)-1] == this.Mins[len(this.Mins)-1] {
		this.Mins = append([]int{}, this.Mins[:len(this.Mins)-1]...)
	}
	this.Stack = append([]int{}, this.Stack[:len(this.Stack)-1]...)
}

func (this *MinStack) Top() int {
	return this.Stack[len(this.Stack)-1]
}

func (this *MinStack) GetMin() int {
	return this.Mins[len(this.Mins)-1]
}
