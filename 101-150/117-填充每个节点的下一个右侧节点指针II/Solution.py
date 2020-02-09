#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个二叉树
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""

class Node(object):

    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):

    # BFS 层次遍历
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        nodes = [root]
        while nodes:
            i = 0
            while i < len(nodes) - 1:
                nodes[i].next = nodes[i+1]
                i += 1
            # 下一层节点
            temp = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            nodes = temp[:]
        return root

def main():
    root = Node(1)
    solution = Solution()
    result = solution.connect(root=root)
    print(result)

if __name__ == "__main__":
    main()
