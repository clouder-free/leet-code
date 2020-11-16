# -*- coding: utf-8 -*-

class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next

def main():
    l1 = ListNode(1)
    l2 = ListNode(2)
    solution = Solution()
    result = solution.mergeTwoLists(l1=l1, l2=l2)

if __name__ == '__main__':
    main()