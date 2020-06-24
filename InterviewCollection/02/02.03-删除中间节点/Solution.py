#! /usr/bin/python

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def deleteNode(self, node):
		p = node.next
		node.next = p.next
		node.val, p.val = p.val, node.val

def main():
	head = ListNode("a")
	n2 = ListNode("b")
	n3 = ListNode("c")
	n4 = ListNode("d")
	n5 = ListNode("e")
	head.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
