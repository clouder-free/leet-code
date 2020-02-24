#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个链表，每个节点包含一个额外增加的随机指针，
该指针可以指向链表中的任何节点或空节点。
要求返回这个链表的深拷贝。 
我们用一个由n个节点组成的链表来表示输入/输出中的链表。
每个节点用一个[val, random_index]表示：
val：一个表示Node.val的整数。
random_index：随机指针指向的节点索引（范围从0到n-1）；如果不指向任何节点，则为null。
"""

class Node(object):

    def __init__(self, x: int, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        nodes = {}
        # 遍历创建新数据
        h = head
        while h:
            node = Node(h.val, None, None)
            nodes[h] = node
            h = h.next
        h = head
        # 遍历建立联系
        while h:
            node = nodes[h]
            if h.next:
                next = nodes[h.next]
                node.next = next
            if h.random:
                random = nodes[h.random]
                node.random = random
            h = h.next
        return nodes[head]

    def copyRandomList2(self, head: Node) -> Node:
        if not head:
            return None
        nodes = {}
        h = head
        while h:
            if h.val in nodes:
                node = nodes.get(h.val)
            else:
                node = Node(h.val, None, None)
            # 下一个节点关系
            if h.next:
                nv = h.next.val
                if nv in nodes:
                    next = nodes.get(nv)
                else:
                    next = Node(nv, None, None)
                    nodes[nv] = next
                node.next = next
            # 随机关系
            if h.random:
                rv = h.random.val
                if rv in nodes:
                    random = nodes.get(rv)
                else:
                    random = Node(rv, None, None)
                    nodes[rv] = random
                node.random = random
            # 添加到nodes
            if node.val not in nodes:
                nodes[node.val] = node
            h = h.next
        return nodes.get(head.val)

def main():
    node = Node(1, None, None)
    solution = Solution()
    result = solution.copyRandomList(head=node)

if __name__ == "__main__":
    main()




