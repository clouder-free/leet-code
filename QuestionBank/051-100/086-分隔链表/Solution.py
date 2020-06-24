#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
你应当保留两个分区中每个节点的初始相对位置。
示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        l, lt = None, None
        r, rt = None, None
        while head:
            if head.val < x:
                if not l:
                    l = head
                    lt = l
                    head = head.next
                    lt.next = None
                else:
                    lt.next = head
                    head = head.next
                    lt = lt.next
                    lt.next = None
            else:
                if not r:
                    r = head
                    rt = r
                    head = head.next
                    rt.next = None
                else:
                    rt.next = head
                    head = head.next
                    rt = rt.next
                    rt.next = None
        # 只有大于x的值
        if not l:
            return r
        # 只有小于x的值
        if not r:
            return l
        # 同时包含有小于和大于x的值
        lt.next = r
        return l

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")

def main():
    head = ListNode(1)
    n1 = ListNode(4)
    n2 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(5)
    n5 = ListNode(2)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    x = 5
    printLinkList(head)
    solution = Solution()
    result = solution.partition(head=head, x=x)
    printLinkList(result)

if __name__ == "__main__":
    main()

