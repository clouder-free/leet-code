#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        i = 0
        while i < len(lists):
            if not lists[i]:
                del lists[i]
                i = 0
            else:
                i += 1
        head = None
        k = None
        print(len(lists))
        while lists:
            index = 0
            for i in range(len(lists)):
                if lists[index].val > lists[i].val:
                    index = i
            if not head or not k:
                head = lists[index]
                k = head
            else:
                k.next = lists[index]
                k = k.next
            # 移动lists[index]
            lists[index] = lists[index].next
            if not lists[index]:
                del lists[index]
        return head

    def mergeKLists2(self, lists: [ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, i, j):
        if i == j:
            return lists[i]
        mid = (i + j) // 2
        left = self.merge(lists, i, mid)
        right = self.merge(lists, mid+1, j)
        return self.mergeTwoList(left, right)

    def mergeTwoList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoList(l1, l2.next)
            return l2

def printLinkList(node):

    print(node.val, end="")
    while node.next:
        print("->", end="")
        node = node.next
        print(node.val, end="")
    print("")


def main():
    l1 = ListNode(1)
    n1 = ListNode(2)
    l1.next = n1
    n2 = ListNode(4)
    n1.next = n2
    l2 = ListNode(1)
    n3 = ListNode(3)
    l2.next = n3
    n4 = ListNode(4)
    n3.next = n4
    l3 = ListNode(2)
    n5 = ListNode(6)
    l3.next = n5
    lists = [l1, None, l2]
    for n in lists:
        if n:
            printLinkList(n)
    solution = Solution()
    results = solution.mergeKLists2(lists=lists)
    # print(results)
    printLinkList(results)

if __name__ == "__main__":
    main()

