#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
输入: [1,3,5,6], 5 输出: 2
输入: [1,3,5,6], 2 输出: 1
输入: [1,3,5,6], 7 输出: 4
输入: [1,3,5,6], 0 输出: 0
"""

class Solution(object):

    def searchInsert(self, nums: [int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1
            else:
                break
        return i


def main():
    nums = [1, 3, 5, 6]
    target = 0
    solution = Solution()
    result = solution.searchInsert(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
nums = [5,7,7,8,8,10], target = 8 [3,4]
nums = [5,7,7,8,8,10], target = 6 [-1,-1]
"""
