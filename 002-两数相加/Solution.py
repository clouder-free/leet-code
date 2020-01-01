#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        value1 = self.listNodeValue(ln=l1)
        value2 = self.listNodeValue(ln=l2)
        print(value1 + value2)
        l3 = self.generateListNode2(value1 + value2)
        self.printListNode(l3)
        # return l3

    def listNodeValue(self, ln):
        if ln.next:
            return ln.val + 10 * self.listNodeValue(ln.next)
        else:
            return ln.val

    def generateListNode(self, value):
        node = ListNode(x=int(value[0]))
        for val in value[1:]:
            parent_node = ListNode(x=int(val))
            parent_node.next = node
            node = parent_node
        return node

    def generateListNode2(self, value):
        val = value % 10
        node = ListNode(x=val)
        if value // 10 != 0:
            node.next = self.generateListNode2(value=value//10)
        return node

    def printListNode(self, node):
        if node:
            print(node.val, end="")
            if node.next:
                print("->", end="")
                self.printListNode(node.next)


class Solution2(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        node = ListNode(x=0)
        n = node
        k = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = k + x + y
            k = total // 10
            n.next = ListNode(total % 10)
            n = n.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if k > 0:
            n.next = ListNode(1)
        # return node
        self.printListNode(node.next)

    def printListNode(self, node):
        if node:
            print(node.val, end="")
            if node.next:
                print("->", end="")
                self.printListNode(node.next)

# [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]


def main():
    l1 = ListNode(1)
    node1 = ListNode(0)
    l1.next = node1
    node2 = ListNode(0)
    node1.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(0)
    node3.next = node4
    node5 = ListNode(0)
    node4.next = node5
    node6 = ListNode(0)
    node5.next = node6
    node7 = ListNode(0)
    node6.next = node7
    node8 = ListNode(0)
    node7.next = node8
    node9 = ListNode(0)
    node8.next = node9
    node10 = ListNode(0)
    node9.next = node10
    node11 = ListNode(0)
    node10.next = node11
    node12 = ListNode(0)
    node11.next = node12
    node13 = ListNode(0)
    node12.next = node13
    node14 = ListNode(0)
    node13.next = node14
    node15 = ListNode(0)
    node14.next = node15
    node16 = ListNode(0)
    node15.next = node16
    node17 = ListNode(0)
    node16.next = node17
    node18 = ListNode(0)
    node17.next = node18
    node19 = ListNode(0)
    node18.next = node19
    node20 = ListNode(0)
    node19.next = node20
    node21 = ListNode(0)
    node20.next = node21
    node22 = ListNode(0)
    node21.next = node22
    node23 = ListNode(0)
    node22.next = node23
    node24 = ListNode(0)
    node23.next = node24
    node25 = ListNode(0)
    node24.next = node25
    node26 = ListNode(0)
    node25.next = node26
    node27 = ListNode(0)
    node26.next = node27
    node28 = ListNode(0)
    node27.next = node28
    node29 = ListNode(0)
    node28.next = node29
    node30 = ListNode(1)
    node29.next = node30
    # node1 = ListNode(4)
    # node2 = ListNode(3)
    # l1.next = node1
    # node1.next = node2
    l2 = ListNode(5)
    node31 = ListNode(6)
    l2.next = node31
    node32 = ListNode(4)
    node31.next = node32
    """
    l1 = ListNode(2)
    node1 = ListNode(4)
    l1.next = node1
    node2 = ListNode(3)
    node1.next = node2
    l2 = ListNode(5)
    node3 = ListNode(6)
    l2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    """

    solution = Solution2()
    solution.addTwoNumbers(l1=l1, l2=l2)

if __name__ == "__main__":
    main()



