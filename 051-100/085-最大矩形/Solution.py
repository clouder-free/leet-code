#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个仅包含0和1的二维二进制矩阵，找出只包含1的最大矩形，并返回其面积。
示例:
输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
"""

class Solution(object):

    def largestRectangleArea(self, heights: [int]) -> int:
        result = 0
        stack = []
        i = 0
        while i < len(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                h = stack.pop()
                if stack:
                    length = i - stack[-1] - 1
                else:
                    length = i
                result = heights[h] * length if heights[h] * length > result else result
            stack.append(i)
            i += 1
        if stack:
            last = stack[-1]
            # 弹出递增序列元素
            while stack:
                h = stack.pop()
                if stack:
                    length = last - stack[-1]
                else:
                    length = last + 1
                result = heights[h] * length if heights[h] * length > result else result
        return result

    def maximalRectangle(self, matrix: [[str]]) -> int:
        result = 0
        rectangle = [[0]*len(matrix[i]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "1":
                    if i == 0:
                        rectangle[i][j] = 1
                    else:
                        rectangle[i][j] = rectangle[i-1][j] + 1
        # 对每一行求取柱状图中最大的矩形
        for rct in rectangle:
            area = self.largestRectangleArea(heights=rct)
            if area > result:
                result = area

        return result

def main():
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    solution = Solution()
    result = solution.maximalRectangle(matrix=matrix)
    print(result)

if __name__ == "__main__":
    main()




