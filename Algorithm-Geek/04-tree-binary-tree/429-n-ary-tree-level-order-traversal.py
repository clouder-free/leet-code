# -*- coding: utf-8 -*-

class Node(object):

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):

    def levelOrder(self, root: Node) -> List[List[int]]:
        result = []
        nodes = [root]
        while nodes:
            values = []
            tmp = []
            for node in nodes:
                values.append(node.val)
                if node.children:
                    tmp.extend(node.children)
            nodes = tmp[:]
            result.append(values)
        return result


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
