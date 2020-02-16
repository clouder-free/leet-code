#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。
找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
输入: [2,2,3,2] 输出: 3
输入: [0,1,0,1,0,1,99] 输出: 99
"""

class Solution(object):

    def singleNumber(self, nums: [int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if len(set(nums[i:i+3])) == 1:
                i += 3
            else:
                return nums[i]
        return nums[i]

def main():
    nums = [0, 1, 1, 1, 99, 99, 99]
    solution = Solution()
    result = solution.singleNumber(nums=nums)
    print(result)

if __name__ == "__main__":
    main()

