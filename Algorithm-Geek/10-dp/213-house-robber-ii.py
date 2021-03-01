# -*- coding: utf-8 -*-

"""
环状房屋
第1个和第n个只能偷一个
"""


class Solution(object):

    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        def my_rob(n):
            dp = [0] * len(n)
            dp[0] = n[0]
            dp[1] = max(n[0], n[1])
            for i in range(2, len(n)):
                dp[i] = max(dp[i-2]+n[i], dp[i-1])
            return dp[-1]
        # 不偷第1个 不偷最后一个
        return max(my_rob(nums[1:]), my_rob(nums[:-1])) if len(nums) > 1 else nums[0]


def main():
    nums = [2, 3, 2]
    nums = [1, 2, 3, 1]
    result = Solution().rob(nums=nums)
    print(result)


if __name__ == '__main__':
    main()
