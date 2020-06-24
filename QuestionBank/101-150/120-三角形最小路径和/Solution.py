#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为11（即，2+3+5+1=11）。
说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""

class Solution(object):

    def minimumTotal(self, triangle: [[int]]) -> int:
        # 从底向上 依次修改赋值
        paths = triangle[-1]
        i = len(triangle) - 2
        while i >= 0:
            for j in range(len(triangle[i])):
                paths[j] = min([paths[j], paths[j+1]]) + triangle[i][j]
            i -= 1
        print(paths)
        return paths[0]

def main():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    solution = Solution()
    result = solution.minimumTotal(triangle=triangle)
    print(result)

if __name__ == "__main__":
    main()
