# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p, q = head, head.next
        p.next = q.next
        q.next = p
        head, r = q, p
        p = p.next
        while p and p.next:
            q = p.next
            p.next = q.next
            q.next = p
            r.next, r = q, p
            p = p.next
        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        h = ListNode(val=0, next=head)
        tail = h
        while head and head.next:
            p = head.next
            head.next, p.next = p.next, head
            tail.next = p
            tail, head = head, head.next
        return h.next


def print_link_list(head):
    while head:
        print(head.val, end='')
        head = head.next
        print('->', end='')
    print('')


def main():
    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print_link_list(head)
    solution = Solution()
    result = solution.swapPairs2(head=head)
    print_link_list(head=result)


if __name__ == '__main__':
    main()


