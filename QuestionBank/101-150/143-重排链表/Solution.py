#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个单链表L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为：L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
给定链表 1->2->3->4, 重新排列为 1->4->2->3.
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        nodes = []
        p = head
        while p:
            nodes.append(p)
            p = p.next
        i, j = 0, len(nodes)-1
        loc = -1
        while i < j:
            nodes[i].next = nodes[j]
            if loc != -1:
                nodes[loc].next = nodes[i]
            loc = j
            i += 1
            j -= 1
        # 奇数个
        if len(nodes) % 2 != 0:
            nodes[loc].next = nodes[i]
            nodes[i].next = None
        # 偶数个
        else:
            nodes[loc].next = None

def main():
    head = ListNode(1)
    solution = Solution()
    solution.reorderList(head=head)

if __name__ == "__main__":
    main()

