#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 递归实现
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        tail = head
        count = 1
        while count < k:
            # print('count', count, 'tail', tail.val)
            tail = tail.next
            if tail:
                count += 1
            else:
                return head

        # 开始执行操作
        current = head
        while head.next != tail:
            i = head.next
            head.next, i.next = i.next, current
            current = i
        head.next, tail.next = tail.next, current
        head, tail = tail, head
        # print('head', head.val, 'tail', tail.val)
        tail.next = self.reverseKGroup(head=tail.next, k=k)
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
    k = 1
    solution = Solution()
    results = solution.reverseKGroup(head=l1, k=k)
    # print(results)
    printLinkList(results)

if __name__ == "__main__":
    main()

