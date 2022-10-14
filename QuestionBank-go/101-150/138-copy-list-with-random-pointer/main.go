package main

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	// node list
	nodes := make(map[*Node]*Node)
	for h := head; h != nil; h = h.Next {
		node := &Node{h.Val, nil, nil}
		nodes[h] = node
	}
	// link nodes
	for h := head; h != nil; h = h.Next {
		if h.Next != nil {
			nodes[h].Next = nodes[h.Next]
		}
		if h.Random != nil {
			nodes[h].Random = nodes[h.Random]
		}
	}
	return nodes[head]
}

func main() {

}
