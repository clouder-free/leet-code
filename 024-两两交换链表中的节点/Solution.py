#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        i = head.next
        # 交换节点
        head.next, i.next = i.next, head
        head, i = i, head
        while i.next and i.next.next:
            j = i.next
            k = j.next
            i.next, j.next, k.next = k, k.next, j
            i = j
        return head

    # 递归实现
    def swapPairsRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        i = head.next
        # 交换节点
        head.next, i.next = i.next, head
        head, i = i, i.next
        i.next = self.swapPairs(head=i.next)
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
    n2 = ListNode(3)
    n1.next = n2
    n3 = ListNode(4)
    n2.next = n3
    printLinkList(l1)
    solution = Solution()
    results = solution.swapPairsRecursive(head=l1)
    # print(results)
    printLinkList(results)

if __name__ == "__main__":
    main()

