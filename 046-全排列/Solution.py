#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):

    def permute(self, nums: [int]) -> [[int]]:
        results = []
        if len(nums) == 1:
            results.append(nums)
            return results

        for i in nums:
            bak = nums[:]
            bak.remove(i)
            right = self.permute(bak)
            for r in right:
                temp = [i]
                temp.extend(r)
                results.append(temp)
        return results

def main():
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.permute(nums=nums)
    print(result)

if __name__ == "__main__":
    main()