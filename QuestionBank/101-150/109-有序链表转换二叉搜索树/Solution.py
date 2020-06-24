#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            root = TreeNode(head.val)
            return root
        last = head.next
        mid = head
        pre_mid = None
        while last:
            last = last.next
            if last:
                last = last.next
                if pre_mid:
                    pre_mid = pre_mid.next
                else:
                    pre_mid = mid
                mid = mid.next
        if pre_mid:
            pre_mid.next = None
        root = TreeNode(mid.val)
        # 左子树
        root.left = self.sortedListToBST(head=head) if pre_mid else None
        # 右子树
        root.right = self.sortedListToBST(head=mid.next) if mid.next else None
        return root

    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        result = []
        if not root:
            return result
        nodes = [root]
        while nodes:
            level_result = []
            temp = []
            # 输出本层节点 并添加下一层的节点
            for node in nodes:
                level_result.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            result.append(level_result)
            nodes = temp[:]
        return result


def main():
    head = ListNode(-10)
    h1 = ListNode(-3)
    h2 = ListNode(0)
    h3 = ListNode(5)
    h4 = ListNode(9)
    head.next = h1
    h1.next = h2
    h2.next = h3
    h3.next = h4
    solution = Solution()
    root = solution.sortedListToBST(head=head)
    result = solution.levelOrderBottom(root=root)
    print(result)

if __name__ == "__main__":
    main()
