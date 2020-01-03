#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
"""
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 1
        h = head
        r = head
        while h.next:
            if i > n:
                r = r.next
            i += 1
            h = h.next
        r.next = r.next.next
        return head

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")

def main():
    node = ListNode(7)
    n1 = ListNode(1)
    node.next = n1
    n2 = ListNode(2)
    n1.next = n2
    n3 = ListNode(3)
    n2.next = n3
    n4 = ListNode(5)
    n3.next = n4
    printLinkList(node)
    n = 5
    solution = Solution()
    result = solution.removeNthFromEnd(head=node, n=n)
    printLinkList(result)

if __name__ == "__main__":
    main()

"""
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""
