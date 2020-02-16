#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def hasCycle(self, head: ListNode) -> bool:
        quick, slow = head, head
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        while head:
            # 判断head值是否为"T"
            if head.val == "T":
                return True
            head.val = "T"
            head = head.next
        return False

def main():
    head = ListNode(1)
    solution = Solution()
    result = solution.hasCycle(head)
    print(result)

if __name__ == "__main__":
    main()




