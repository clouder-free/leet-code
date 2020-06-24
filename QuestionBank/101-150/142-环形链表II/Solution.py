#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果pos是 -1，则在该链表中没有环。
说明：不允许修改给定的链表。
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None

def main():
    head = ListNode(1)
    solution = Solution()
    result = solution.detectCycle(head=head)
    if result:
        print(result.val)
    else:
        print("None")

if __name__ == "__main__":
    main()
