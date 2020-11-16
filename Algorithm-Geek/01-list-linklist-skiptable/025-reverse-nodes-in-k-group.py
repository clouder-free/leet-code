# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        h = ListNode(0)
        h.next = head
        pre = h
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return h.next
            nex = tail.next
            head, tail = self.reverseLinkList(head, tail)
            pre.next = head
            pre = tail
            head = nex
        return h.next

    def reverseLinkList(self, head, tail):
        pre = tail.next
        p = head
        while pre != tail:
            q = p.next
            p.next = pre
            pre = p
            p = q
        return pre, head

def printLinkList(head):
    while head:
        print(head.val, '->', end='')
        head = head.next
    print()

def main():
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    printLinkList(head=head)
    solution = Solution()
    result = solution.reverseKGroup(head=head, k=3)
    printLinkList(result)

if __name__ == '__main__':
    main()



