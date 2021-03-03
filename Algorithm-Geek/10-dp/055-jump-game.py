# -*- coding: utf-8 -*-

class Solution(object):

    def canJump(self, nums: [int]) -> bool:
        if not nums:
            return False
        dp = [False] * len(nums)
        j = len(nums)-1
        for i in range(j-1, -1, -1):
            if nums[i] >= j-i:
                dp[i] = True
                j = i
        return dp[0]


def main():
    nums = [2, 3, 1, 1, 4]
    result = Solution().canJump(nums=nums)
    print(result)


if __name__ == '__main__':
    main()
