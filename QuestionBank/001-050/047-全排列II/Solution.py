#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):

    def permuteUnique(self, nums: [int]) -> [[int]]:
        results = []
        def back_trace(nums, temp):
            if not nums:
                results.append(temp)
                return
            for i in range(len(nums)):
                if nums[i] in nums[:i]:
                    continue
                back_trace(nums[:i]+nums[i+1:], temp+[nums[i]])
        back_trace(nums, [])
        return results

def main():
    nums = [3, 3, 0, 3]
    solution = Solution()
    result = solution.permuteUnique(nums=nums)
    print(result)

if __name__ == "__main__":
    main()