#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定n个非负整数 a1，a2，...，an,
每个数代表坐标中的一个点(i,ai)
在坐标内画n条垂直线,垂直线i的两个端点分别为(i,ai)和(i,0)
找出其中的两条线,使得它们与x轴共同构成的容器可以容纳最多的水
说明:你不能倾斜容器且n的值至少为2
"""

class Solution(object):

    def maxArea(self, height: [int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            area = min(height[right], height[left]) * (right - left) if min(height[right], height[left]) * (right - left) > area else area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maxArea(height=height)
    print(result)

if __name__ == "__main__":
    main()

"""
"""
