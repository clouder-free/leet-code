#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表，旋转链表，将链表每个节点向右移动k个位置，其中k是非负数。
示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        # 构成链表环
        length = 1
        p = head
        while p.next:
            p = p.next
            length += 1
        k %= length
        if k == 0:
            return head
        p.next = head
        step = length - k - 1
        p = head
        while step > 0:
            p = p.next
            step -= 1
        head = p.next
        p.next = None
        return head

def print_list_node(head):

    while head:
        print(head.val, end="")
        head = head.next
        if head:
            print("->", end="")
    print("")

def main():
    # head = ListNode(1)
    # n2 = ListNode(2)
    # n3 = ListNode(3)
    # n4 = ListNode(4)
    # n5 = ListNode(5)
    # head.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    head = ListNode(1)
    n2 = ListNode(2)
    head.next = n2
    print_list_node(head)
    solution = Solution()
    result = solution.rotateRight(head=head, k=2)
    print_list_node(result)

if __name__ == "__main__":
    main()

