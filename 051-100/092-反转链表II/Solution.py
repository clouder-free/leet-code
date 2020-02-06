#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        length = n - m + 1
        h = head
        l = None
        while m - 1:
            l = h
            h = h.next
            m -= 1

        tail = h
        nh = None
        while length:
            temp = h.next
            h.next = nh
            nh = h
            h = temp
            length -= 1
        if l:
            l.next = nh
        else:
            head = nh
        tail.next = h
        return head

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")

def main():
    m, n = 2, 4
    head = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l4 = ListNode(5)
    head.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    printLinkList(head)
    solution = Solution()
    result = solution.reverseBetween(head=head, m=m, n=n)
    printLinkList(result)

if __name__ == "__main__":
    main()
