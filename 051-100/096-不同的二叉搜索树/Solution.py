#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
C(n+1) = 2 * C(n) * (2*n+1) / (n+2)
"""

class Solution(object):

    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(n):
            c = 2 * c * (2*i + 1) / (i+2)
        return int(c)

def main():
    n = 3
    solution = Solution()
    result = solution.numTrees(n=n)
    print(result)

if __name__ == "__main__":
    main()

