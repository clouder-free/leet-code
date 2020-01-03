#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个包含n个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和d
使得a+b+c+d的值与target相等？找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):

    def fourSum(self, nums: [int], target: int) -> [[int]]:
        results = []
        nums.sort()
        for i in range(len(nums)-3):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            threes = self.threeSum(nums=nums[i+1:], target=target - nums[i])
            print("i:", i, "three_result:", threes)
            if threes:
                for t in threes:
                    t.append(nums[i])
                results.extend([t for t in threes])
        return results

    def threeSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return result



def main():
    nums = [-1, 0, 1, 2, -1, -4]
    target = -1
    solution = Solution()
    result = solution.fourSum(nums=nums, target=target)
    print(result)
    # results = spliceCombinations(s)
    # print(results)


if __name__ == "__main__":
    main()

"""
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
