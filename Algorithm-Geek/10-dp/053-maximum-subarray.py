# -*- coding: utf-8 -*-

class Solution(object):

    def maxSubArray(self, nums: [int]) -> int:
        result = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            if current > result:
                result = current
        return result

    def maxSubArray2(self, nums: [int]) -> int:
        # dp
        result, pre = nums[0], 0
        for i in range(len(nums)):
            pre = max(pre+nums[i], nums[i])
            result = max(pre, result)
        return result


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [1]
    solution = Solution()
    result = solution.maxSubArray(nums=nums)
    print(result)


if __name__ == '__main__':
    main()
