package main

// double linked list
type DLinkList struct {
	Key   int
	Value int
	Pre   *DLinkList
	Next  *DLinkList
}

type LRUCache struct {
	Cache    map[int]*DLinkList
	Head     *DLinkList
	Tail     *DLinkList
	Capacity int
	Size     int
}

func Constructor(capacity int) LRUCache {
	head := &DLinkList{}
	tail := &DLinkList{}
	head.Next = tail
	tail.Pre = head
	return LRUCache{
		Cache:    make(map[int]*DLinkList),
		Head:     head,
		Tail:     tail,
		Capacity: capacity,
	}
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.Cache[key]; ok {
		this.moveToHead(node)
		return node.Value
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.Cache[key]; ok {
		// update node value
		node.Value = value
		this.moveToHead(node)
	} else {
		node := &DLinkList{key, value, nil, nil}
		this.addToHead(node)
		this.Cache[key] = node
		this.Size += 1
		if this.Size > this.Capacity {
			// remove linklist and update cache
			tail := this.removeTail()
			delete(this.Cache, tail.Key)
			this.Size -= 1
		}
	}

}

func (this *LRUCache) moveToHead(node *DLinkList) {
	this.removeNode(node)
	this.addToHead(node)
}

func (this *LRUCache) addToHead(node *DLinkList) {
	node.Pre = this.Head
	node.Next = this.Head.Next
	this.Head.Next.Pre = node
	this.Head.Next = node
}

func (this *LRUCache) removeNode(node *DLinkList) {
	node.Pre.Next = node.Next
	node.Next.Pre = node.Pre
}

func (this *LRUCache) removeTail() *DLinkList {
	node := this.Tail.Pre
	this.removeNode(node)
	return node
}
