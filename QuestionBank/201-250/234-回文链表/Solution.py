# -*- coding: utf-8 -*-
"""
回文链表
"""

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        return nodes == nodes[::-1]


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
