package main

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

func connect(root *Node) *Node {
	if root == nil {
		return root
	}
	nodes := []*Node{root}
	for len(nodes) > 0 {
		tmp := []*Node{}
		for i := 0; i < len(nodes)-1; i++ {
			nodes[i].Next = nodes[i+1]
			if nodes[i].Left != nil {
				tmp = append(tmp, nodes[i].Left)
			}
			if nodes[i].Right != nil {
				tmp = append(tmp, nodes[i].Right)
			}
		}
		if nodes[len(nodes)-1].Left != nil {
			tmp = append(tmp, nodes[len(nodes)-1].Left)
		}
		if nodes[len(nodes)-1].Right != nil {
			tmp = append(tmp, nodes[len(nodes)-1].Right)
		}
		nodes = tmp[:]
	}
	return root
}

func connect2(root *Node) *Node {
	if root == nil {
		return root
	}
	p := root
	for p != nil {
		var head, tail *Node
		for p != nil {
			if p.Left != nil {
				if head == nil {
					head, tail = p.Left, p.Left
				} else {
					tail.Next = p.Left
					tail = tail.Next
				}
			}
			if p.Right != nil {
				if head == nil {
					head, tail = p.Right, p.Right
				} else {
					tail.Next = p.Right
					tail = tail.Next
				}
			}
			p = p.Next
		}
		p = head
	}
	return root
}
