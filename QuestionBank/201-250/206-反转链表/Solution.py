# -*- coding: utf-8 -*-

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # 从头到尾
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 辅助节点
        new_head = ListNode(0)
        new_head.next = head
        while head.next:
            p, q = new_head.next, head.next
            new_head.next = q
            head.next = q.next
            q.next = p
        return new_head.next

    # 迭代
    def reverseList2(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p
        return prev

    # 递归
    def reverseList3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return p


def print_list_node(root):
    while root:
        print(root.val, end=' ')
        root = root.next
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
    print_list_node(root=head)
    result = Solution().reverseList3(head=head)
    print_list_node(result)


if __name__ == '__main__':
    main()

