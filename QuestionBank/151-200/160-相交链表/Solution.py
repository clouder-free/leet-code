#! /usr/bin/python

"""
编写一个程序，找到两个单链表相交的起始节点。
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0)。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
"""

class ListNode(object):
    
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        while headA or headB:
            if headA:
                if headA in nodes:
                    return headA
                else:
                    nodes.add(headA)
                    headA = headA.next
            if headB:
                if headB in nodes:
                    return headB
                else:
                    nodes.add(headB)
                    headB = headB.next
        return None

def main():
    """
    headA = ListNode(4)
    n1 = ListNode(1)
    n2 = ListNode(8)
    n3 = ListNode(4)
    n4 = ListNode(5)
    headA.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    headB = ListNode(5)
    n5 = ListNode(0)
    n6 = ListNode(1)
    headB.next = n5
    n5.next = n6
    n6.next = n2
    """
    headA = ListNode(2)
    n1 = ListNode(6)
    n2 = ListNode(4)
    headA.next = n1
    n1.next = n2
    headB = ListNode(1)
    n3 = ListNode(5)
    headB.next = n3
    solution = Solution()
    result = solution.getIntersectionNode(headA=headA, headB=headB)
    if result:
        print(result.val)
    else:
        print('None')

if __name__ == '__main__':
    main()


