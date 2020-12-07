# -*- coding: utf-8 -*-

class Solution(object):

    def maxSubArray(self, nums: [int]) -> int:
        result = nums[0]
        current = nums[0]
        for i in range(len(nums)):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            if current > result:
                result = current
        return result


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    result = solution.maxSubArray(nums=nums)
    print(result)


if __name__ == '__main__':
    main()
