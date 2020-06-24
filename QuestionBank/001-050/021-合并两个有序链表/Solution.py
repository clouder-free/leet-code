#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        k = head
        while l1 and l2:
            if l1.val < l2.val:
                k.next = l1
                l1 = l1.next
            else:
                k.next = l2
                l2 = l2.next
            k = k.next

        while l1:
            k.next = l1
            l1 = l1.next
            k = k.next
        while l2:
            k.next = l2
            l2 = l2.next
            k = k.next

        return head

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")

def main():
    l1 = ListNode(1)
    n1 = ListNode(2)
    l1.next = n1
    n2 = ListNode(4)
    # n1.next = n2
    l2 = ListNode(1)
    n3 = ListNode(3)
    l2.next = n3
    n4 = ListNode(4)
    n3.next = n4
    printLinkList(l1)
    printLinkList(l2)
    solution = Solution()
    result = solution.mergeTwoLists(l1=l1, l2=l2)
    printLinkList(result)

if __name__ == "__main__":
    main()

"""
输入：([)] 输出：false
"""
