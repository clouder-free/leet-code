# -*- coding: utf-8 -*-

class Solution(object):

    # 动态规划dp
    def lengthOfLIS(self, nums: [int]) -> int:
        length = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
            if length < dp[i]:
                length = dp[i]
        # print(dp)
        return length


def main():
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [0, 1, 0, 3, 2, 3]
    nums = [7, 7, 7, 7, 7, 7]
    solution = Solution()
    result = solution.lengthOfLIS(nums=nums)
    print(result)


if __name__ == '__main__':
    main()



