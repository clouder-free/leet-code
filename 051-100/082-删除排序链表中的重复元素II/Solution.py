#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
示例 1:
输入: 1->2->3->3->4->4->5  输出: 1->2->5
示例 2:
输入: 1->1->1->2->3  输出: 2->3
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        i, j = head, head.next
        head, tail = None, None
        while j:
            if i.val != j.val:
                if not head:
                    head, tail = i, i
                else:
                    tail.next = i
                    tail = tail.next
                i = j
                j = i.next
            else:
                while j and i.val == j.val:
                    j = j.next
                i = j
                if i:
                    j = i.next
        if i:
            if head:
                tail.next = i
                tail = tail.next
            else:
                head, tail = i, i
        if tail:
            tail.next = None
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
