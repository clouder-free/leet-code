# -*- coding: utf-8 -*-
"""
分割等和子集
"""

class Solution:

    # dp
    def canPartition(self, nums: [int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total//2
        # row col
        m, n = len(nums), target+1
        dp = [[False] * n for _ in range(m)]
        # 第0行
        if nums[0] <= target:
            dp[0][nums[0]] = True
        # 填表
        for i in range(1, m):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                elif nums[i] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
