#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
输入: 1->1->2 输出: 1->2
输入: 1->1->2->3->3 输出: 1->2->3
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        i = head
        while i.next:
            if i.val == i.next.val:
                i.next = i.next.next
            else:
                i = i.next
        return head

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")

def main():
    head = ListNode(1)
    l1 = ListNode(1)
    l2 = ListNode(2)
    # l3 = ListNode(2)
    # l4 = ListNode(3)
    # l5 = ListNode(4)
    # l6 = ListNode(5)
    head.next = l1
    l1.next = l2
    # l2.next = l3
    # l3.next = l4
    # l4.next = l5
    # l5.next = l6
    printLinkList(head)
    solution = Solution()
    result = solution.deleteDuplicates(head=head)
    printLinkList(result)

if __name__ == "__main__":
    main()
