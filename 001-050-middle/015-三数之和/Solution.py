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
        # 排序 避免重复
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            others = set()
            for j in range(i+1, len(nums)-1):
                if nums[j] not in others:
                    others.add(nums[j])
                    if (target - nums[j]) in set(nums[j+1:]):
                        result.append([nums[i], nums[j], target - nums[j]])
        return result

    def threeSum2(self, nums: [int]) -> [[int]]:
        # 排序 避免重复
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    # 移动j k
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return result

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum2(nums=nums)
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
