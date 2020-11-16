# -*- coding: utf-8 -*-

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p, head.next = head.next, None
        while p:
            q = p.next
            p.next = head
            head = p
            p = q
        return head

    # 双指针
    def reverseList2(self, head: ListNode) -> ListNode:
        p, q = None, head
        while q:
            k = q.next
            q.next = p
            p, q = q, k
        return p

def print_link_list(head):
    while head:
        print(head.val, end='')
        head = head.next
        print('->', end='')
    print('')

def main():
    solution = Solution()
    head = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n4 = ListNode(5)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print_link_list(head=head)
    result = solution.reverseList2(head=head)
    print_link_list(result)

if __name__ == '__main__':
    main()

