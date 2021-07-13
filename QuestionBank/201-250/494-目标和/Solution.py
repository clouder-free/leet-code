# -*- coding: utf-8 -*-
"""
目标和
"""

class Solution:

    # 超时
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        result = 0
        def _dfs(nums, target):
            nonlocal result
            if not nums:
                if target == 0:
                    result += 1
                return
            _dfs(nums[1:], target+nums[0])
            _dfs(nums[1:], target-nums[0])
        _dfs(nums, target)
        return result

    # dp
    def findTargetSumWays2(self, nums: [int], target: int) -> int:
        total = sum(nums)
        if total < target or (total + target) % 2:
            return 0
        t = (total + target) // 2
        dp = [0] * (t+1)
        dp[0] = 1
        for num in nums:
            for j in range(t, num-1, -1):
                dp[j] += dp[j-num]
        return dp[-1]


def main():
    nums = [1, 1, 1, 1, 1]
    target = 3
    result = Solution().findTargetSumWays2(nums, target)
    print(result)


if __name__ == '__main__':
    main()
