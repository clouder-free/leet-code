#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
"""

class Solution(object):

    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1, -1]
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                m = mid
                while i < m:
                    left = (m + i) // 2
                    if nums[left] == target:
                        m = left
                    else:
                        i = left + 1
                n = mid
                while n < j:
                    right = (n + j) // 2 + 1
                    if nums[right] == target:
                        n = right
                    else:
                        j = right - 1
                return [m, n]
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return [-1, -1]


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    solution = Solution()
    result = solution.searchRange(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
nums = [5,7,7,8,8,10], target = 8 [3,4]
nums = [5,7,7,8,8,10], target = 6 [-1,-1]
"""
