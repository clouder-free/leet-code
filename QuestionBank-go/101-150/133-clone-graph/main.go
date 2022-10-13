package main

type Node struct {
	Val       int
	Neighbors []*Node
}

var nodeMap map[int]*Node

func cloneGraph(node *Node) *Node {
	if node == nil {
		return nil
	}
	nodeMap = make(map[int]*Node)
	return clone(node)
}

func clone(node *Node) *Node {
	if node == nil {
		return nil
	}
	if nodeMap[node.Val] != nil {
		return nodeMap[node.Val]
	}
	n := &Node{node.Val, []*Node{}}
	nodeMap[node.Val] = n
	for i := 0; i < len(node.Neighbors); i++ {
		n.Neighbors = append(n.Neighbors, clone(node.Neighbors[i]))
	}
	return n
}
