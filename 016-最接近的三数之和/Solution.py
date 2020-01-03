#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个包括n个整数的数组nums和一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):

    def threeSumClosest(self, nums: [int], target: int) -> int:
        # 排序 避免重复
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                # abs相减判断，res替换更接近target的值
                if abs(result - target) > abs(temp - target):
                    result = temp
                # 判断是left右移还是right左移
                if temp > target:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
        return result

def main():
    nums = [-1, 0, 1, 1, 55]
    target = 3
    solution = Solution()
    result = solution.threeSumClosest(nums=nums, target=target)
    print(result)

if __name__ == "__main__":
    main()

"""
nums = [-1，2，1，-4] target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
