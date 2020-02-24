#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入: [2,1,5,6,2,3]
输出: 10
"""

class Solution:

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

def main():
    # heights = [2, 1, 5, 6, 2, 3]
    heights = [0, 9]
    solution = Solution()
    result = solution.largestRectangleArea(heights=heights)
    print(result)

if __name__ == "__main__":
    main()
