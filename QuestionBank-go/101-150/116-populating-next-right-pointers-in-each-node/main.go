package main

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

// level traveral
func connect(root *Node) *Node {
	if root == nil || root.Left == nil {
		return root
	}
	nodes := []*Node{root.Left, root.Right}
	for len(nodes) > 0 {
		tmp := []*Node{}
		for i := 0; i < len(nodes)-1; i++ {
			nodes[i].Next = nodes[i+1]
			if nodes[i].Left != nil {
				tmp = append(tmp, nodes[i].Left, nodes[i].Right)
			}
		}
		if nodes[len(nodes)-1].Left != nil {
			tmp = append(tmp, nodes[len(nodes)-1].Left, nodes[len(nodes)-1].Right)
		}
		nodes = tmp[:]
	}
	return root
}

// recursion
func connect2(root *Node) *Node {
	return connectNodes(root, nil)
}

func connectNodes(root *Node, sibling *Node) *Node {
	if root == nil || root.Left == nil {
		return root
	}
	// root left and right
	root.Left.Next = root.Right
	// sibling Node
	if sibling != nil {
		root.Right.Next = sibling.Left
	}
	// recurse root.Left
	connectNodes(root.Left, root.Right)
	// recurse root.Right
	if sibling != nil {
		connectNodes(root.Right, sibling.Left)
	} else {
		connectNodes(root.Right, nil)
	}

	return root
}

// recursion
func connect3(root *Node) *Node {
	if root == nil || root.Left == nil {
		return root
	}
	p := root
	for p != nil {
		q := p
		for q != nil && q.Left != nil {
			// q left link to right
			q.Left.Next = q.Right
			if q.Next != nil {
				q.Right.Next = q.Next.Left
			}
			q = q.Next
		}
		p = p.Left
	}
	return root
}
