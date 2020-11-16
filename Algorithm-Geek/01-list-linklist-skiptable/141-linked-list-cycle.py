# -*- coding: utf-8 -*-


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        p, q = head, head.next
        while p and q:
            p = p.next
            q = q.next
            if q:
                q = q.next
                if p == q:
                    return True
            else:
                return False
        return False


def main():
    head = ListNode(3)
    n1 = ListNode(2)
    n2 = ListNode(0)
    n3 = ListNode(-4)
    head.next = n1
    n1.next = head
    # n1.next = n2

    # n2.next = n3
    # n3.next = n1
    solution = Solution()
    result = solution.hasCycle(head=head)
    print(result)

if __name__ == '__main__':
    main()

