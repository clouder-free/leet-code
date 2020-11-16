# -*- coding: utf-8 -*-


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None


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

