#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得a+b+c=0?找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[[-1, 0, 1],[-1, -1, 2]]
"""

class Solution(object):

    def threeSum(self, nums: [int]) -> [[int]]:
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        pass
        return []

def main():
    strs = ["dog", "racecar", "car"]
    solution = Solution()
    result = solution.threeSum(nums=strs)
    print(result)

if __name__ == "__main__":
    main()

"""
nums = [-1, 0, 1, 2, -1, -4]
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
