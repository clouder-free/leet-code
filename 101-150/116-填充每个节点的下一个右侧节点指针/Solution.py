#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。
"""

class Node(object):

    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):

    def connect(self, root: Node) -> Node:
        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.next
        return root

    def connect2(self, root: Node) -> Node:
        if not root:
            return None
        nodes = [root]
        while nodes:
            i = 0
            while i < len(nodes) - 1:
                nodes[i].next = nodes[i+1]
                i += 1
            # 每层最后一个节点置空
            nodes[i].next = None
            # 下一层节点
            temp = []
            for node in nodes:
                # 如果为空 退出
                if not node.left or not node.right:
                    break
                temp.append(node.left)
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
