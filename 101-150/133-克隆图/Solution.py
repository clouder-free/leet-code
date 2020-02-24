#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给你无向连通图中一个节点的引用，请你返回该图的深拷贝（克隆）。
图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
class Node {
    public int val;
    public List<Node> neighbors;
}
简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1，第二个节点值为 2，
以此类推。该图在测试用例中使用邻接列表表示。
邻接列表是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
给定节点将始终是图中的第一个节点（值为 1）。你必须将给定节点的拷贝作为对克隆图的引用返回。
"""

class Node(object):

    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution(object):

    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        nodes = {}
        visited = set()
        queue = [node]
        while queue:
            q = queue.pop(0)
            if q.val not in visited:
                visited.add(q.val)
                if q.val not in nodes:
                    n = Node(q.val)
                else:
                    n = nodes.get(q.val)
                # 创建邻居关系
                for neighbor in q.neighbors:
                    nv = neighbor.val
                    if nv not in nodes:
                        neibor = Node(nv)
                        nodes[nv] = neibor
                    else:
                        neibor = nodes.get(nv)
                    n.neighbors.append(neibor)
                    # 将q的邻居加入队列中
                    queue.append(neighbor)
                # 将n添加到nodes中
                if n.val not in nodes:
                    nodes[n.val] = n
        return nodes[node.val]

def main():
    node = Node(1)
    solution = Solution()
    result = solution.cloneGraph(node=node)
    print(result)

if __name__ == "__main__":
    main()


