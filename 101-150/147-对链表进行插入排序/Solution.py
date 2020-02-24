#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
对链表进行插入排序。
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
输入: 4->2->1->3  输出: 1->2->3->4
输入: -1->5->3->4->0  输出: -1->0->3->4->5
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def insertionSortList(self, head: ListNode) -> ListNode:
        p = head
        head, tail = None, None
        while p:
            if not head:
                head = p
                tail = p
                p = p.next
                tail.next = None
            else:
                q = p
                p = p.next
                if q.val <= head.val:
                    q.next = head
                    head = q
                elif head.val < q.val < tail.val:
                    k = head
                    while k.next.val < q.val:
                        k = k.next
                    q.next = k.next
                    k.next = q
                else:
                    tail.next = q
                    tail = q
                    tail.next = None
        return head

def main():
    head = ListNode(4)
    l1 = ListNode(2)
    l2 = ListNode(1)
    l3 = ListNode(3)
    head.next = l1
    l1.next = l2
    l2.next = l3
    solution = Solution()
    result = solution.insertionSortList(head=head)
    while result:
        print(result.val,)
        result = result.next

if __name__ == "__main__":
    main()


