#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
输入: [2,3,1,1,4]  输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为0跳到下标为1的位置，跳1步，然后跳3步到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
"""

class Solution(object):

    def jump(self, nums: [int]) -> int:
        if nums.count(1) == len(nums):
            return len(nums)-1
        def fun(n):
            if not n:
                return 0
            for k, v in enumerate(n):
                if v + k >= len(n):
                    return fun(n[:k]) + 1
        return fun(nums[:-1])


    # 动态规划 从前向后
    def jump3(self, nums: [int]) -> int:
        position = len(nums) - 1
        step = 0
        while position != 0:
            for i in range(position):
                if nums[i] + i >= position:
                    position = i
                    step += 1
                    break
        return step

    # 动态规划 从后向前超时
    def jump2(self, nums: [int]) -> int:
        # 从当前位置跳跃最少次数到达最后一个位置
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            # 判断nums[i]是否为0
            if nums[i] == 0:
                # 置为最大
                dp[i] = len(nums)
            elif i + nums[i] >= len(nums)-1:
                dp[i] = 1
            else:
                dp[i] = min(dp[i+1:i+nums[i]+1]) + 1
        return dp[0]

def main():
    nums = [2, 3, 0, 1, 4]
    solution = Solution()
    result = solution.jump(nums=nums)
    print(result)

if __name__ == "__main__":
    main()

