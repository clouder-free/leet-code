#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
输入: [1,2,0] 输出: 3
输入: [3,4,-1,1] 输出: 2
输入: [7,8,9,11,12] 输出: 1
"""

class Solution(object):

    # 考虑时间复杂度和空间复杂度
    def firstMissingPositive(self, nums: [int]) -> int:
        if 1 not in nums:
            return 1
        # 保证非负
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        # 判断
        for i in range(len(nums)):
            loc = abs(nums[i]) - 1
            if nums[loc] > 0:
                nums[loc] = -nums[loc]

        # 第一个正数的下标+1为所求
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1

        # 都为负数
        return len(nums)+1

    # 只考虑时间复杂度 不考虑空间复杂度
    def firstMissingPositive2(self, nums: [int]) -> int:
        numset = set()
        for num in nums:
            if num > 0:
                numset.add(num)
        i = 1
        while i <= len(nums):
            if i not in numset:
                break
            i += 1
        return i

def main():
    nums = [-1, 2, 0]
    solution = Solution()
    result = solution.firstMissingPositive(nums=nums)
    print(result)

if __name__ == "__main__":
    main()
