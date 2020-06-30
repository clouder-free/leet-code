#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
输入: [2,3,1,1,4] 输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
输入: [3,2,1,0,4] 输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""

class Solution(object):

    def canJump(self, nums: [int]) -> bool:
        # 判断i之前元素的value
        def judgeZero(nums, i):
            j = 0
            while j < i:
                if nums[j] > i - j:
                    return True
                j += 1
            return False
        if len(nums) <= 1:
            return True
        if nums[0] == 0:
            return False
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                # 判断i之前元素的value 跳不过去就返回错误
                if not judgeZero(nums, i):
                    return False
            i += 1
        return True
    
    def canJump2(self, nums: [int]) -> bool:
        i, max_pos = 0, 0
        for i in range(len(nums)):
            if max_pos < i:
                continue
            max_pos = max(max_pos, i+nums[i])
            if max_pos >= len(nums)-1:
                return True
        return False


def main():
    nums = [3, 0, 0, 0]
    solution = Solution()
    result = solution.canJump2(nums=nums)
    print(result)

if __name__ == "__main__":
    main()
