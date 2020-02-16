#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""

class Solution(object):

    # 左右双指针
    def trap(self, height: [int]) -> int:
        if not height or len(height) == 1:
            return 0
        result = 0
        l, r = 0, len(height)-1
        lmax, rmax = 0, 0
        while l < r:
            if height[l] < height[r]:
                lmax = max([lmax, height[l]])
                result += lmax - height[l]
                l += 1
            else:
                rmax = max([rmax, height[r]])
                result += rmax - height[r]
                r -= 1
        return result

def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    result = solution.trap(height=height)
    print(result)

if __name__ == "__main__":
    main()



