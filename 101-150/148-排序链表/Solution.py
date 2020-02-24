#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
在O(nlogn)时间复杂度和常数级空间复杂度下，对链表进行排序。
输入: 4->2->1->3  输出: 1->2->3->4
输入: -1->5->3->4->0  输出: -1->0->3->4->5
"""
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        p, q = head, head
        while q and q.next:
            pre = p
            p = p.next
            q = q.next.next
        n1 = self.sortList(pre.next)
        pre.next = None
        n2 = self.sortList(head)
        return self.merge_nodes(n1=n1, n2=n2)

    def merge_nodes(self, n1, n2):
        head = ListNode(0)
        p = head
        while n1 or n2:
            if not n1:
                p.next = n2
                n2 = n2.next
            elif not n2:
                p.next = n1
                n1 = n1.next
            elif n1.val < n2.val:
                p.next = n1
                n1 = n1.next
            else:
                p.next = n2
                n2 = n2.next
            p = p.next
        return head.next


def main():
    head = ListNode(1)
    solution = Solution()
    result = solution.sortList(head=head)
    print(result)

if __name__ == "__main__":
    main()

