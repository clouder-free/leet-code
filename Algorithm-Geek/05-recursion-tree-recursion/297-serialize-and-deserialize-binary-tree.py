# -*- coding: utf-8 -*-

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec(object):

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'X'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(lst):
            if not lst:
                return None
            val = lst.pop(0)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = dfs(lst)
            root.right = dfs(lst)
            return root
        return dfs(data.split(','))



